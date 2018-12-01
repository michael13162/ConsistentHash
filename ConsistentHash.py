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

from Simulator import Simulator
from TestCase import TestCase

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Fall 2018 CS5150/CS6150 Consistent Hashing Project Simulator.  Command to try: python3.6 ConsistentHash.py --file-size=20 --file-count=100000 --num-clients=5000 --num-caches=10 --simulation-length=100 --cache-resources=100000")
    parser.add_argument("--file-size", action='store', type=int, required=True,
                        help="Simulated request file size (Bytes)")
    parser.add_argument("--file-count", action='store', type=int, required=True,
                        help="Number of distinct files")
    parser.add_argument("--num-clients", action='store', type=int, required=True,
                        help="Number of simulated clients")
    parser.add_argument("--num-caches", action='store', type=int, required=True,
                        help="Number of simulated caches")
    parser.add_argument("--simulation-length", action='store', type=int, required=True,
                        help="Number of simulation steps")
    parser.add_argument("--cache-resources", action='store', type=int, required=True,
                        help="Available bandwidth on each cache")

    args = parser.parse_args()

    case = TestCase.generate_test_case(
        file_size=args.file_size,
        file_count=args.file_count,
        num_clients=args.num_clients,
        num_caches=args.num_caches,
        simulation_length=args.simulation_length,
        cache_resources=args.cache_resources,
        cuckoo=False
    )

    simulator = Simulator(case)
    trace = simulator.run()
    simulator.visualize(trace)

    case = TestCase.generate_test_case(
        file_size=args.file_size,
        file_count=args.file_count,
        num_clients=args.num_clients,
        num_caches=args.num_caches,
        simulation_length=args.simulation_length,
        cache_resources=args.cache_resources,
        cuckoo=True
    )

    simulator = Simulator(case)
    trace = simulator.run()
    simulator.visualize(trace)
