# ConsistentHash

This project simulates a content network with several caches and many
clients. The goal of the simulation is to experiment with how different
optimizations affect the load balancing of the cache nodes

## Setup
Main executable: `ConsistentHash.py`

If you don't already have the appropriate libraries installed, they are
listed in `requirements.txt`. We recommend setting up a virtual
environment:
 1. Run `virtualenv env` to initialize the virtual environment.
   - Make sure that this will give a Python 3 environment!
   - Some Linux distributions package a `virtualenv-3` variant which
   will use the latest Python 3. Other times, you might need to use a
   command line flag, like `virtualenv -p /usr/bin/python3 env`
 2. Enter the virtual environment with `source env/bin/activate`
   - When you are finished, either exit the shell session or use
   `deactivate`
 3. Install the dependencies in the environment with
    `pip install -r requirements.txt`

Run `ConsistentHash.py --help` for command-line parameter descriptions

After the simulation runs, image files with the simulation results will be written to the working directory.

## Features:
  - Consistent hashing, as described by Karger et al.
  - Two-point load-balancing hash function as discussed in class
    - Further discussed here: https://brooker.co.za/blog/2012/01/17/two-random.html
    - Before executing a request, the client queries the load on both
      visible cache. The actual request is delivered to the
      less-loaded cache
    - In case of a complete cache miss, the client is assumed to know
      the true address of the root server, and makes a query there
      directly
