# Copyright 2019 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import collections
import contextlib
import itertools

import attr

from ... import util
from ...step_data import StepData


class StepRunner(object):
  """A StepRunner is the interface to actually running steps.

  These can actually make subprocess calls (SubprocessStepRunner), or just
  pretend to run the steps with mock output (SimulationStepRunner).
  """
  @property
  def stream_engine(self):
    """Return the stream engine that this StepRunner uses, if meaningful.

    Users of this method must be prepared to handle None.
    """
    return None

  def open_step(self, step_config):
    """Constructs an OpenStep object which can be used to actually run a step.

    Args:
      step_config (StepConfig): The step data.

    Returns: an OpenStep object.
    """
    raise NotImplementedError()

  @contextlib.contextmanager
  def run_context(self):
    """A context in which the entire engine run takes place.

    This is typically used to catch exceptions thrown by the recipe.
    """
    yield


class OpenStep(object):
  """An object that can be used to run a step.

  We use this object instead of just running directly because, after a step
  is run, it stays open (can be modified with step_text and links and things)
  until another step at its nest level or lower is started.
  """
  def run(self):
    """Starts the step, running its command."""
    raise NotImplementedError()

  def finalize(self):
    """Closes the step and finalizes any stored presentation."""
    raise NotImplementedError()

  @property
  def stream(self):
    """The stream.StepStream that this step is using for output.

    It is permitted to use this stream between run() and finalize() calls. """
    raise NotImplementedError()


# Placeholders associated with a rendered step.
Placeholders = collections.namedtuple('Placeholders',
    ('inputs_cmd', 'outputs_cmd', 'stdout', 'stderr', 'stdin'))

# Result of 'render_step'.
#
# Fields:
#   config (StepConfig): The step configuration.
#   placeholders (Placeholders): Placeholders for this rendered step.
#   followup_annotations (list): A list of followup annotation, populated during
#       simulation test.
RenderedStep = collections.namedtuple('RenderedStep',
    ('config', 'placeholders', 'followup_annotations'))


# Singleton object to indicate a value is not set.
UNSET_VALUE = object()


def render_step(step_config, step_test):
  """Renders a step so that it can be fed to annotator.py.

  Args:
    step_config (StepConfig): The step config to render.
    step_test: The test data json dictionary for this step, if any.
               Passed through unaltered to each placeholder.

  Returns (RenderedStep): the rendered step, including a Placeholders object
      representing any placeholder instances that were found while rendering.
  """
  # Process 'cmd', rendering placeholders there.
  input_phs = collections.defaultdict(lambda: collections.defaultdict(list))
  output_phs = []
  new_cmd = []
  for item in (step_config.cmd or ()):
    if isinstance(item, util.Placeholder):
      module_name, placeholder_name = item.namespaces
      tdata = step_test.pop_placeholder(
          module_name, placeholder_name, item.name)
      new_cmd.extend(item.render(tdata))
      if isinstance(item, util.InputPlaceholder):
        input_phs[module_name][placeholder_name].append((item, tdata))
      else:
        assert isinstance(item, util.OutputPlaceholder), (
            'Not an OutputPlaceholder: %r' % item)
        output_phs.append((item, tdata))
    else:
      new_cmd.append(item)
  step_config = attr.evolve(step_config, cmd=new_cmd)

  # Process 'stdout', 'stderr' and 'stdin' placeholders, if given.
  stdio_placeholders = {}
  for key in ('stdout', 'stderr', 'stdin'):
    placeholder = getattr(step_config, key)
    tdata = None
    if placeholder:
      if key == 'stdin':
        assert isinstance(placeholder, util.InputPlaceholder), (
            '%s(%r) should be an InputPlaceholder.' % (key, placeholder))
      else:
        assert isinstance(placeholder, util.OutputPlaceholder), (
            '%s(%r) should be an OutputPlaceholder.' % (key, placeholder))
      tdata = getattr(step_test, key)
      placeholder.render(tdata)
      assert placeholder.backing_file is not None
      step_config = attr.evolve(step_config, **{key:placeholder.backing_file})
    stdio_placeholders[key] = (placeholder, tdata)

  return RenderedStep(
      config=step_config,
      placeholders=Placeholders(
          inputs_cmd=input_phs,
          outputs_cmd=output_phs,
          **stdio_placeholders),
      followup_annotations=None,
  )


def construct_step_result(rendered_step, retcode):
  """Constructs a StepData step result from step return data.

  The main purpose of this function is to add output placeholder results into
  the step result where output placeholders appeared in the input step.
  Also give input placeholders the chance to do the clean-up if needed.
  """
  step_result = StepData(rendered_step.config, retcode)

  try:
    # Input placeholders inside step |cmd|.
    placeholders = rendered_step.placeholders
    for _, pholders in placeholders.inputs_cmd.iteritems():
      for _, items in pholders.iteritems():
        for ph, td in items:
          ph.cleanup(td.enabled)

    # Output placeholders inside step |cmd|.
    for pholder, test_data in placeholders.outputs_cmd:
      step_result.assign_placeholder(
          pholder, pholder.result(step_result.presentation, test_data))

    # Placeholders that are used with IO redirection.
    for key in ('stdout', 'stderr', 'stdin'):
      ph, td = getattr(placeholders, key)
      if ph:
        if isinstance(ph, util.OutputPlaceholder):
          setattr(step_result, key, ph.result(step_result.presentation, td))
        else:
          assert isinstance(ph, util.InputPlaceholder), (
              '%s(%r) should be an InputPlaceholder.' % (key, ph))
          ph.cleanup(td.enabled)
  finally:
    step_result.finalize()

  return step_result