# Copyright 2022 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

from recipe_engine import post_process

DEPS = [
    'assertions',
    'buildbucket',
    'cv',
    'properties',
]


def RunSteps(api):
  api.assertions.assertEqual(api.cv.owner_is_googler,
                             api.properties['expected_owner_is_googler'])


def GenTests(api):
  yield (api.test('default') + api.cv(run_mode=api.cv.FULL_RUN) +
         api.buildbucket.try_build(project='chrome') +
         api.properties(expected_owner_is_googler=False) +
         api.post_process(post_process.DropExpectation))
  yield (api.test('is googler') +
         api.cv(run_mode=api.cv.FULL_RUN, owner_is_googler=True) +
         api.buildbucket.try_build(project='chrome') +
         api.properties(expected_owner_is_googler=True) +
         api.post_process(post_process.DropExpectation))
  yield (api.test('chrome-branch-project') + api.cv(run_mode=api.cv.FULL_RUN) +
         api.buildbucket.try_build(project='chrome-m100') +
         api.properties(expected_owner_is_googler=False) +
         api.post_process(post_process.DropExpectation))
  yield (api.test('raise if not Chrome') + api.cv(run_mode=api.cv.FULL_RUN) +
         api.buildbucket.try_build(project='infra') +
         api.expect_exception('ValueError') +
         api.post_process(post_process.DropExpectation))
