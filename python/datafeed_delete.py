#!/usr/bin/python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Deletes a datafeed from the specified account."""

from __future__ import print_function
import argparse
import sys

import shopping_common

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('datafeed_id', help='The ID of the datafeed to delete.')


def main(argv):
  # Authenticate and construct service.
  service, config, flags = shopping_common.init(
      argv, __doc__, parents=[argparser])
  merchant_id = config['merchantId']
  datafeed_id = flags.datafeed_id

  request = service.datafeeds().delete(
      merchantId=merchant_id, datafeedId=datafeed_id)
  request.execute()
  print('Datafeed %s was deleted.' % datafeed_id)


if __name__ == '__main__':
  main(sys.argv)
