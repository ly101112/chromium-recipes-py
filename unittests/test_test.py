#!/usr/bin/env python
# Copyright 2017 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)
import recipe_engine.env


from recipe_engine import package
from recipe_engine import package_pb2


class RecipeWriter(object):
  """Helper to write a recipe for tests."""

  def __init__(self, recipes_dir, name):
    self.recipes_dir = recipes_dir
    self.name = name

    # These are expected to be set appropriately by the caller.
    self.DEPS = []
    self.RunStepsLines = ['pass']
    self.GenTestsLines = ['yield api.test("basic")']
    self.expectations = {}

  @property
  def expect_dir(self):
    return os.path.join(self.recipes_dir, '%s.expected' % self.name)

  def add_expectation(self, test_name, commands=None, recipe_result=None,
                      status_code=0):
    """Adds expectation for a simulation test.

    Arguments:
      test_name(str): name of the test
      commands(list): list of expectation dictionaries
      recipe_result(object): expected result of the recipe
      status_code(int): expected exit code
    """
    self.expectations[test_name] = (commands or []) + [{
        'name': '$result',
        'recipe_result': recipe_result,
        'status_code': status_code
    }]

  def write(self):
    """Writes the recipe to disk."""
    dirs = [self.recipes_dir]
    # Only create expectation directory if we have any expectations.
    if self.expectations:
      dirs.append(self.expect_dir)
    for d in dirs:
      if not os.path.exists(d):
        os.makedirs(d)
    with open(os.path.join(self.recipes_dir, '%s.py' % self.name), 'w') as f:
      f.write('\n'.join([
        'from recipe_engine import post_process',
        '',
        'DEPS = %r' % self.DEPS,
        '',
        'def RunSteps(api):',
      ] + ['  %s' % l for l in self.RunStepsLines] + [
        '',
        'def GenTests(api):',
      ] + ['  %s' % l for l in self.GenTestsLines]))
    for test_name, test_contents in self.expectations.iteritems():
      name = ''.join('_' if c in '<>:"\\/|?*\0' else c for c in test_name)
      with open(os.path.join(self.expect_dir, '%s.json' % name), 'w') as f:
        json.dump(test_contents, f)


class RecipeModuleWriter(object):
  """Helper to write a recipe module for tests."""

  def __init__(self, root_dir, name):
    self.root_dir = root_dir
    self.name = name

    # These are expected to be set appropriately by the caller.
    self.DEPS = []
    self.disable_strict_coverage = False
    self.methods = {}

    self.example = RecipeWriter(self.module_dir, 'example')

  @property
  def module_dir(self):
    return os.path.join(self.root_dir, 'recipe_modules', self.name)

  def write(self):
    """Writes the recipe module to disk."""

    if not os.path.exists(self.module_dir):
      os.makedirs(self.module_dir)

    with open(os.path.join(self.module_dir, '__init__.py'), 'w') as f:
      f.write('DEPS = %r\n' % self.DEPS)
      if self.disable_strict_coverage:
        f.write('\nDISABLE_STRICT_COVERAGE = True')

    api_lines = [
        'from recipe_engine import recipe_api',
        '',
        'class MyApi(recipe_api.RecipeApi):',
    ]
    if self.methods:
      for m_name, m_lines in self.methods.iteritems():
        api_lines.extend([
            '',
            '  def %s(self):' % m_name,
          ] + ['    %s' % l for l in m_lines] + [
            '',
          ])
    else:
      api_lines.append('  pass')
    with open(os.path.join(self.module_dir, 'api.py'), 'w') as f:
      f.write('\n'.join(api_lines))


class TestTest(unittest.TestCase):
  def setUp(self):
    root_dir = tempfile.mkdtemp()
    config_dir = os.path.join(root_dir, 'infra', 'config')
    os.makedirs(config_dir)

    self._root_dir = root_dir
    self._recipes_cfg = os.path.join(config_dir, 'recipes.cfg')
    self._recipe_tool = os.path.join(ROOT_DIR, 'recipes.py')

    test_pkg = package_pb2.Package(
        api_version=1,
        project_id='test_pkg',
        recipes_path='',
        deps=[
            package_pb2.DepSpec(
                project_id='recipe_engine',
                url='file://'+ROOT_DIR),
        ],
    )
    package.ProtoFile(self._recipes_cfg).write(test_pkg)

  def tearDown(self):
    shutil.rmtree(self._root_dir)

  def _run_recipes(self, *args):
    return subprocess.check_output((
        sys.executable,
        self._recipe_tool,
        '--use-bootstrap',
        '--package', self._recipes_cfg,
    ) + args, stderr=subprocess.STDOUT)

  def test_list(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.write()
    json_path = os.path.join(self._root_dir, 'tests.json')
    self._run_recipes('test', 'list', '--json', json_path)
    with open(json_path) as f:
      json_data = json.load(f)
    self.assertEqual(
        {'format': 1, 'tests': ['foo.basic']},
        json_data)

  def test_test(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run')

  def test_test_expectation_failure_empty(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertNotIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertNotIn('CHECK(FAIL)', cm.exception.output)
    self.assertIn(
        'foo.basic failed',
        cm.exception.output)

  def test_test_expectation_failure_different(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.DEPS = ['recipe_engine/step']
    rw.RunStepsLines = ['api.step("test", ["echo", "bar"])']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertNotIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertNotIn('CHECK(FAIL)', cm.exception.output)
    self.assertIn(
        'foo.basic failed',
        cm.exception.output)
    self.assertIn(
        '+[{\'cmd\': [\'echo\', \'bar\'], \'name\': \'test\'},\n',
        cm.exception.output)

  def test_test_expectation_pass(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.DEPS = ['recipe_engine/step']
    rw.RunStepsLines = ['api.step("test", ["echo", "bar"])']
    rw.add_expectation('basic', [{'cmd': ['echo', 'bar'], 'name': 'test'}])
    rw.write()
    self._run_recipes('test', 'run')

  def test_test_recipe_not_covered(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['if False:', '  pass']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertNotIn('CHECK(FAIL)', cm.exception.output)
    self.assertNotIn('foo.basic failed', cm.exception.output)

  def test_test_check_failure(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.MustRun, "bar")'
    ]
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertNotIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertIn('CHECK(FAIL)', cm.exception.output)
    self.assertIn('foo.basic failed', cm.exception.output)

  def test_test_check_success(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.DoesNotRun, "bar")'
    ]
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run')

  def test_test_recipe_syntax_error(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['baz']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('NameError: global name \'baz\' is not defined',
                  cm.exception.output)

  def test_test_recipe_module_uncovered(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo')
    mw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('The following modules lack test coverage: foo',
                  cm.exception.output)

  def test_test_recipe_module_syntax_error(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['foo'] = ['baz']
    mw.write()
    mw.example.DEPS = ['foo_module']
    mw.example.RunStepsLines = ['api.foo_module.foo()']
    mw.example.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('NameError: global name \'baz\' is not defined',
                  cm.exception.output)
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)

  def test_test_recipe_module_syntax_error_in_example(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['foo'] = ['pass']
    mw.write()
    mw.example.DEPS = ['foo_module']
    mw.example.RunStepsLines = ['baz']
    mw.example.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('NameError: global name \'baz\' is not defined',
                  cm.exception.output)
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)

  def test_test_recipe_module_example_not_covered(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['foo'] = ['pass']
    mw.write()
    mw.example.DEPS = ['foo_module']
    mw.example.RunStepsLines = ['if False:', '  pass']
    mw.example.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)

  def test_test_recipe_module_uncovered_not_strict(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo')
    mw.disable_strict_coverage = True
    mw.write()
    self._run_recipes('test', 'run')

  def test_test_recipe_module_covered_by_recipe_not_strict(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['bar'] = ['pass']
    mw.disable_strict_coverage = True
    mw.write()
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo_recipe')
    rw.DEPS = ['foo_module']
    rw.RunStepsLines = ['api.foo_module.bar()']
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run')

  def test_test_recipe_module_covered_by_recipe(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['bar'] = ['pass']
    mw.write()
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo_recipe')
    rw.DEPS = ['foo_module']
    rw.RunStepsLines = ['api.foo_module.bar()']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('The following modules lack test coverage: foo_module',
                  cm.exception.output)

  def test_test_recipe_module_partially_covered_by_recipe_not_strict(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['bar'] = ['pass']
    mw.methods['baz'] = ['pass']
    mw.disable_strict_coverage = True
    mw.write()
    mw.example.DEPS = ['foo_module']
    mw.example.RunStepsLines = ['api.foo_module.baz()']
    mw.example.add_expectation('basic')
    mw.example.write()
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo_recipe')
    rw.DEPS = ['foo_module']
    rw.RunStepsLines = ['api.foo_module.bar()']
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run')

  def test_test_recipe_module_partially_covered_by_recipe(self):
    mw = RecipeModuleWriter(self._root_dir, 'foo_module')
    mw.methods['bar'] = ['pass']
    mw.methods['baz'] = ['pass']
    mw.write()
    mw.example.DEPS = ['foo_module']
    mw.example.RunStepsLines = ['api.foo_module.baz()']
    mw.example.add_expectation('basic')
    mw.example.write()
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo_recipe')
    rw.DEPS = ['foo_module']
    rw.RunStepsLines = ['api.foo_module.bar()']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)

  def test_train_basic(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run', '--train')

  def test_train_missing(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.write()
    self.assertFalse(os.path.exists(rw.expect_dir))
    self._run_recipes('test', 'run', '--train')
    self.assertTrue(os.path.exists(rw.expect_dir))
    expect_path = os.path.join(rw.expect_dir, 'basic.json')
    self.assertTrue(os.path.exists(expect_path))
    with open(expect_path) as f:
      expect_contents = json.load(f)
    self.assertEqual(
        [{u'status_code': 0, u'recipe_result': None, u'name': u'$result'}],
        expect_contents)

  def test_train_diff(self):
    # 1. Initial state: recipe expectations are passing.
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.write()
    self._run_recipes('test', 'run')

    # 2. Change the recipe and verify tests would fail.
    rw.DEPS = ['recipe_engine/step']
    rw.RunStepsLines = ['api.step("test", ["echo", "bar"])']
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn('foo.basic failed', cm.exception.output)

    # 3. Make sure training the recipe succeeds and produces correct results.
    self._run_recipes('test', 'run', '--train')
    expect_path = os.path.join(rw.expect_dir, 'basic.json')
    with open(expect_path) as f:
      expect_contents = json.load(f)
    self.assertEqual(
        [{u'cmd': [u'echo', u'bar'], u'name': u'test'},
         {u'status_code': 0, u'recipe_result': None, u'name': u'$result'}],
        expect_contents)

  def test_train_checks_coverage(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['if False:', '  pass']
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run', '--train')
    self.assertIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertNotIn('CHECK(FAIL)', cm.exception.output)
    self.assertNotIn('foo.basic failed', cm.exception.output)

  def test_train_runs_checks(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.MustRun, "bar")'
    ]
    rw.add_expectation('basic')
    rw.write()
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run', '--train')
    self.assertNotIn('FATAL: Insufficient coverage', cm.exception.output)
    self.assertIn('CHECK(FAIL)', cm.exception.output)
    self.assertIn('foo.basic failed', cm.exception.output)

  def test_unused_expectation_file_test(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.add_expectation('unused')
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'unused.json')
    self.assertTrue(os.path.exists(expectation_file))
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn(
        'FATAL: unused expectations found:\n%s' % expectation_file,
        cm.exception.output)
    self.assertTrue(os.path.exists(expectation_file))

  def test_unused_expectation_file_train(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.add_expectation('unused')
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'unused.json')
    self.assertTrue(os.path.exists(expectation_file))
    self._run_recipes('test', 'run', '--train')
    self.assertFalse(os.path.exists(expectation_file))

  def test_drop_expectation_test(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.DropExpectation)'
    ]
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'basic.json')
    self.assertFalse(os.path.exists(expectation_file))
    self._run_recipes('test', 'run')
    self.assertFalse(os.path.exists(expectation_file))

  def test_drop_expectation_train(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.DropExpectation)'
    ]
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'basic.json')
    self.assertFalse(os.path.exists(expectation_file))
    self._run_recipes('test', 'run', '--train')
    self.assertFalse(os.path.exists(expectation_file))

  def test_drop_expectation_test_unused(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.DropExpectation)'
    ]
    rw.add_expectation('basic')
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'basic.json')
    self.assertTrue(os.path.exists(expectation_file))
    with self.assertRaises(subprocess.CalledProcessError) as cm:
      self._run_recipes('test', 'run')
    self.assertIn(
        'FATAL: unused expectations found:\n%s\n%s' % (
            rw.expect_dir, expectation_file),
        cm.exception.output)
    self.assertTrue(os.path.exists(expectation_file))

  def test_drop_expectation_train_unused(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = [
        'yield api.test("basic") + \\',
        '  api.post_process(post_process.DropExpectation)'
    ]
    rw.add_expectation('basic')
    rw.write()
    expectation_file = os.path.join(rw.expect_dir, 'basic.json')
    self.assertTrue(os.path.exists(expectation_file))
    self._run_recipes('test', 'run', '--train')
    self.assertFalse(os.path.exists(expectation_file))
    self.assertFalse(os.path.exists(rw.expect_dir))

  def test_unused_expectation_preserves_owners_test(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.write()
    owners_file = os.path.join(rw.expect_dir, 'OWNERS')
    with open(owners_file, 'w') as f:
      pass
    self.assertTrue(os.path.exists(owners_file))
    self._run_recipes('test', 'run')
    self.assertTrue(os.path.exists(owners_file))

  def test_unused_expectation_preserves_owners_train(self):
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.add_expectation('basic')
    rw.write()
    owners_file = os.path.join(rw.expect_dir, 'OWNERS')
    with open(owners_file, 'w') as f:
      pass
    self.assertTrue(os.path.exists(owners_file))
    self._run_recipes('test', 'run', '--train')
    self.assertTrue(os.path.exists(owners_file))

  def test_test_slash_in_name(self):
    test_name = 'bar/baz'
    rw = RecipeWriter(os.path.join(self._root_dir, 'recipes'), 'foo')
    rw.RunStepsLines = ['pass']
    rw.GenTestsLines = ['yield api.test(%r)' % test_name]
    rw.add_expectation(test_name)
    rw.write()
    self._run_recipes('test', 'run')


if __name__ == '__main__':
  sys.exit(unittest.main())
