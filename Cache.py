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

# Filename:    Cache.py
# Date:        27 November 2018
# Description: Class representing a cache which hosts Files and accepts requests from Clients

from collections import namedtuple
import typing

from SimulatorFile import SimulatorFile


LoadReply = namedtuple('LoadReply', ['load', 'has_file'])


class Cache:

    def __init__(self, total_resources: float, token: int, misses_to_add: int, files: dict):
        self.total_request_counter = 0
        self.accepted_requests_counter = 0
        self.used_resources = 0
        self.total_resources = total_resources
        self.token = token
        self.requests_per_file = {}
        self.misses_to_add = misses_to_add
        self.hosted_files = files
        self.miss_count = 0

    def reset(self):
        """
        Clear all per-timestep information in the Cache to prepare for the next timestep
        """
        self.total_request_counter = 0
        self.accepted_requests_counter = 0
        self.used_resources = 0
        self.requests_per_file = {}
        self.miss_count = 0
        return

    def accept_request(self, file: SimulatorFile) -> LoadReply:
        self.total_request_counter += 1

        load = (self.used_resources / self.total_resources) * 100
        value = self.hosted_files.get(file.key)
        if value == None:
            self.hosted_files[file.key] = 1
            self.miss_count += 1
            return LoadReply(load, False)
        if value < self.misses_to_add:
            self.hosted_files[file.key] += 1
            self.miss_count += 1
            return LoadReply(load, False)
        return LoadReply(load, True)

    def handle_request(self, file: SimulatorFile, bandwidth: float = None):
        self.accepted_requests_counter += 1
        self.used_resources += file.size

    def __repr__(self):
        return str(self.token)
