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

# Filename:    TestCase.py
# Date:        28 November 2018
# Description: Class representing all the parameters of an individual test case

import random
from typing import List, Optional

import SimulatorFile


class TestCase:

    @staticmethod
    def generate_test_case(file_size: int,
                           file_count: int,
                           num_clients: int,
                           num_caches: int,
                           simulation_length: int,
                           cache_resources: int,
                           distribution_function) -> 'TestCase':
        """
        Generate a new, random test case
        """
        files = [SimulatorFile.generate_random_file(file_size) for i in range(file_count)]

        # Generate sequence of client file requests
        request_sequences = [[]] * num_clients
        for client in range(num_clients):
            request_sequence = [None] * simulation_length
            # Test code: Every client has an 80% chance of requesting a file on a particular timestep
            # Each file has a uniform-random chance to be selected
            # TODO: Select files based on realistic distribution
            for timestep in range(simulation_length):
                file_requested = random.random() < 0.8
                file = distribution_function(len(files))
                request_sequence[timestep] = file if file_requested else None
            request_sequences[client] = request_sequence

        # Generate tokens for each cache
        cache_tokens = [random.randint(0, SimulatorFile.MAX_HASH_VALUE) for cache in range(num_caches)]

        cache_resources = [cache_resources] * num_caches

        return TestCase(files, num_clients, num_caches, simulation_length, request_sequences, cache_tokens, cache_resources)

    def __init__(self,
                 files: List[SimulatorFile.SimulatorFile],
                 num_clients: int,
                 num_caches: int,
                 simulation_length: int,
                 request_sequences: List[List[Optional[int]]],
                 cache_tokens: List[int],
                 cache_resources: List[float]):
        self.files = files
        self.num_clients = num_clients
        self.num_caches = num_caches
        self.simulation_length = simulation_length
        self.request_sequences = request_sequences
        self.cache_tokens = cache_tokens
        self.cache_resources = cache_resources
