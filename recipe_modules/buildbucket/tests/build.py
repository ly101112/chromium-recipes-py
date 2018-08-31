# Copyright 2018 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import json

from google.protobuf import text_format

DEPS = [
  'buildbucket',
  'properties',
  'step',
]


def RunSteps(api):
  text = text_format.MessageToString(api.buildbucket.build)
  api.step('dummy', ['echo'] + text.splitlines())


def GenTests(api):

  def case(name, **properties):
    return api.test(name) + api.properties(**properties)

  def legacy_build(name, **buildbucket_build):
    return case(name, buildbucket={'build': buildbucket_build})

  yield case('empty')

  yield case('serialized buildbucket property', buildbucket=json.dumps({
    'build': {'id': '123456789'}
  }))

  yield legacy_build('v1 build with id', id='123456789')

  yield legacy_build('v1 empty buildset', tags=['buildset:'])
  yield legacy_build('v1 unknown buildset format', tags=['buildset:x'])

  yield legacy_build('v1 gerrit change', tags=[
      'buildset:patch/gerrit/chromium-review.googlesource.com/1/2',
  ])

  yield legacy_build('v1 gitiles commit', tags=[
      ('buildset:commit/gitiles/chromium.googlesource.com/chromium/src/+/'
       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
  ])
  yield legacy_build('v1 gitiles commit, invalid', tags=[
      'buildset:commit/gitiles/a/b/c/d'
  ])

  yield case(
      'buildbot gitiles commit',
      repository='https://chromium.googlesource.com/v8/v8.git',
      branch='refs/heads/master',
      revision='a' * 40,
  )
  yield case(
      'buildbot gitiles commit, invalid repo URL',
      repository='ftp://chromium.googlesource.com/v8/v8.git',
  )
  yield case(
      'buildbot gitiles commit, a project prefix',
      repository='https://chromium.googlesource.com/a/v8/v8.git',
      branch='refs/heads/master',
      revision='a' * 40,
  )
  yield case(
      'buildbot gitiles commit, branch',
      repository='https://chromium.googlesource.com/v8/v8.git',
      branch='master',
      revision='a' * 40,
  )
  yield case(
      'buildbot gitiles commit, invalid repo',
      repository='https://invalid/',
      branch='master',
      revision='a' * 40,
  )
  yield case(
      'buildbot gitiles commit, no branch',
      repository='https://chromium.googlesource.com/v8/v8.git',
      revision='a' * 40,
  )
  yield case(
      'buildbot gitiles commit, HEAD revision',
      repository='https://chromium.googlesource.com/v8/v8.git',
      branch='refs/heads/master',
      revision='HEAD',
  )
  yield case(
      'buildbot gitiles commit, no revision',
      repository='https://chromium.googlesource.com/v8/v8.git',
      branch='refs/heads/master',
  )
  yield case(
      'buildbot gitiles commit, neither ref nor revision',
      repository='https://chromium.googlesource.com/v8/v8.git',
  )

  yield legacy_build(
      'v1 luci builder id',
      project='chromium',
      bucket='luci.chromium.try',
      tags=['builder:linux'])

  yield case(
      'v1 buildbot builder id', mastername='chromium', buildername='linux')

  yield legacy_build('v1 tags', tags=['a:b', 'c:d'])
  yield legacy_build('v1 hidden tags', tags=[
      'buildset:patch/gerrit/chromium-review.googlesource.com/1/2',
      ('buildset:commit/gitiles/chromium.googlesource.com/chromium/src/+/'
       'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'),
      'build_address:bucket/builder/123',
      'builder:linux',
  ])