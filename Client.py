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

# Filename:    Client.py
# Date:        27 November 2018
# Description: Class representing a client which makes requests against a Cache

from typing import List

from SimulatorFile import SimulatorFile
from Cache import Cache


class Client:

    def __init__(self, visible_caches: List[Cache], request_sequence: List[int]):
        """
        Construct a new client

        :param visible_caches: List of caches available to this Client
        :param request_sequence: List of indicies into the current TestCase's file list which this Client will request per timestep
        """
        self.visible_caches = sorted(visible_caches, key=lambda c: c.token)
        self.request_sequence = request_sequence
        self.complete_misses = 0
        pass

    def reset(self):
        """
        Clear all per-timestep information in the Client to prepare for the next timestep
        """
        self.complete_misses = 0
        return

    def make_request(self, file: SimulatorFile, cuckoo):
        # Get hash codes from file
        hash1: int = file.hash1()
        hash2: int = file.hash2()

        # Select server (Call 'accept_request' to both)
        cache1 = self.consistent_hash(hash1)
        if cuckoo:
            cache2 = self.consistent_hash(hash2)

        response1 = cache1.accept_request(file)
        if cuckoo:
            response2 = cache2.accept_request(file)

        # Taking into account whether the server actually has the file or not,
        # we make the request
        if cuckoo:
            if response1.has_file and (not response2.has_file or response1.load < response2.load):
                cache1.handle_request(file)
            elif response2.has_file and (not response1.has_file or response2.load <= response1.load):
                cache2.handle_request(file)
            else:
                self.complete_misses += 1
        else:
            if response1.has_file:
                cache1.handle_request(file)

    def consistent_hash(self, hash: int) -> Cache:
        """
        Apply the consistent hashing algorithm from Karger et. al to get the server
        which should be hosting this hash code

        :param hash: Hash code of the file we want
        :return: Cache into whose range this hash lands
        """

        # Linear search to find the proper Cache
        for idx in range(len(self.visible_caches)):
            cache = self.visible_caches[idx]
            if hash < cache.token:
                # This hash value falls into the range of this cache
                return cache
        return self.visible_caches[-1]
