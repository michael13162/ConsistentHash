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

# Filename:    Simulator.py
# Date:        28 November 2018
# Description: Class which runs one ConsistentHash simulation

from Cache import Cache
from Client import Client
from TestCase import TestCase
import matplotlib.pyplot as plt


class Simulator:

    def __init__(self, test_case: TestCase):
        self.test_case = test_case
        self.caches = [Cache(resources, token) for resources, token in zip(self.test_case.cache_resources, self.test_case.cache_tokens)]
        self.clients = [Client(self.caches, requests) for requests in self.test_case.request_sequences]

    def run(self):
        trace = {}
        for cache in self.caches:
            trace[cache.token] = []

        # Do the simulator loop, for as long as the TestCase specifies
        for timestep in range(self.test_case.simulation_length):
            # Prepare all clients and caches for the new timestep
            for cache in self.caches: cache.reset()
            for client in self.clients: client.reset()

            # Run simulation step
            for client in self.clients:
                file_idx = client.request_sequence[timestep]
                if file_idx is not None:
                    client.make_request(self.test_case.files[file_idx], self.test_case.cuckoo)

            for cache in self.caches:
                trace[cache.token].append((cache.used_resources, cache.total_request_counter, cache.accepted_requests_counter))

        return trace


    def visualize(self, trace):
        ratios = []

        for timestep in range(self.test_case.simulation_length):
            loads = sorted([trace[cache.token][timestep][0] for cache in self.caches])
            ratios.append(loads[len(self.caches) - 1] / loads[0])

        print(ratios)

        fig = plt.figure()
        plt.plot(ratios)
        plt.title('Simulation results with ' + str(len(self.clients)) + ' clients, ' + str(len(self.caches)) + ' caches, and cuckoo=' + str(self.test_case.cuckoo))
        plt.xlabel('timestep')
        plt.ylabel('max load / min load ratio')
        fig.savefig('cuckoo_' + str(self.test_case.cuckoo) + '.png')

