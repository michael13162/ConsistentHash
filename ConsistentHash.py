#!/usr/bin/env python3

# Copyright 2018 Jeremy Whipple
# Copyright 2018 Simon Redman
# Copyright 2018 Michael Zhang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Filename:    ConsistentHash.py
# Date:        28 November 2018
# Description: Main executable for the ConsistentHash project

import argparse
import json

from Simulator import Simulator
from TestCase import TestCase


case = TestCase.generate_test_case(100, 20, 20, 5, 10, 1000)

simulator = Simulator(case)

simulator.run()

pass