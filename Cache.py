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

    def __init__(self, total_resources: float):
        self.total_request_counter = 0
        self.accpted_request_counter = 0
        self.total_resources = total_resources
        self.requests_per_file = {}

    def accept_request(self, file: SimulatorFile) -> LoadReply:
        self.total_request_counter += 1

        return LoadReply(None, True)

    def handle_request(self, bandwidth: float):
        pass
