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

import hashlib
import random
import string


MAX_HASH_VALUE = 2**256 - 1  # SHA256 = 256 bits


SALT1 = "JSM"
SALT2 = "WRZ"


def generate_random_file(size: int, key_length: int = 20) -> 'SimulatorFile':
    key = str.join('', random.choices(string.ascii_letters + string.digits, k=key_length))
    return SimulatorFile(key, size)


class SimulatorFile:

    def __init__(self, key: str, size: int):
        self.key = key
        self.size = size

    def hash1(self) -> int:
        input = self.key + SALT1
        return self._hash(input)

    def hash2(self) -> int:
        input = self.key + SALT2
        return self._hash(input)

    def _hash(self, input: str) -> int:
        hash = hashlib.sha256(input.encode())
        return int(hash.hexdigest(), 16)

    def __repr__(self):
        return self.key