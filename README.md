# ConsistentHash

This project simulates a content network with several caches and many
clients. The goal of the simulation is to experiment with how different
optimizations affect the load balancing of the cache nodes

Main executable: `ConsistentHash.py`

Run `ConsistentHash.py --help` for command-line parameter descriptions

After the simulation runs, you should be greeted with pretty graphs
summarizing the results of the experiment!

Features:
  - Consistent hashing, as described by Karger et al.
  - Two-point load-balancing hash function as discussed in class
    - Further discussed here: https://brooker.co.za/blog/2012/01/17/two-random.html
    - Before executing a request, the client queries the load on both
      visible cache. The actual request is delivered to the
      less-loaded cache
    - In case of a complete cache miss, the client is assumed to know
      the true address of the root server, and makes a query there
      directly
