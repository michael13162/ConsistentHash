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

# Filename:    SimulatorFile.py
# Date:        28 November 2018
# Description: Class representing a file which resides on one or more Servers and is requested by Clients


class SimulatorFile:
    SALT1 = "JSM"
    SALT2 = "WRZ"

    def __init__(self, key: str, size: int):
        self.key = key
        self.size = size

    def hash1(self) -> int:
        pass

    def hash2(self) -> int:
        pass
