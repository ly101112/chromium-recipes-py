#!/usr/bin/env vpython3
# Copyright 2020 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

"""Automatically updates the client libraries sourced from luci-py."""

import json
import os
import tarfile

import requests


BASE_URL = 'https://chromium.googlesource.com/infra/luci/luci-py'
LOG_URL = BASE_URL+'/+log/main/client/libs?format=JSON&n=1'
TAR_URL = BASE_URL+'/+archive/%s/client/libs.tar.gz'


def main():
  """Automatically updates the client libraries in this directory."""
  base_dir = os.path.abspath(os.path.dirname(__file__))

  resp = requests.get(LOG_URL)
  head_commit = str(json.loads(resp.text[4:])['log'][0]['commit'])
  print('Updating client libs to %r' % (head_commit,))

  resp = requests.get(TAR_URL % (head_commit,), stream=True).raw
  with tarfile.open(mode='r|*', fileobj=resp) as tar:
    for item in tar:
      if item.name.endswith(('_test.py','OWNERS',)):
        print('Skipping file: %r' % item.name)
        continue
      elif os.path.basename(item.name) == 'tests' and item.isdir():
        print('Skipping folder: %r' % item.name)
        continue
      else:
        # In case people run it from another directory
        tar.extract(item, path=base_dir)

  with open(os.path.join(base_dir, 'README.md'), 'w') as rmd:
    print('// Generated by update.py. DO NOT EDIT.', file=rmd)
    print('Client libraries copied from', file=rmd)
    print(BASE_URL+'/+/'+head_commit+'/client/libs', file=rmd)

  print('Done.')


if __name__ == '__main__':
  main()
