## Overview 

Original task:
```
Given a start point and an end point and a list of gateway line segments, find the shortest path from start to end that goes through gateway segments in order.
```
### Observations & Algorithm
* We're not limited in number of turns, and they're cost us nothing, we care only about minifying total distance
* Therefore, aiming for empty space is unnecessary; it’s always optimal to target gate pillars or the final destination
* From any given point, we can only aim for a subset of points visible through all intermediate gates
* This constraint allows us to construct a directed graph with a manageable number of nodes and edges
* A modified Dijkstra’s algorithm can then be applied to find the shortest valid path

### Implementation
* Core part of the algorithm is in `path.py`
* Logic of identifying is point visible or not is in `visibility.py`
* Basic tests are in `path_tests.py`

## How to run

### Prerequest
`pip install -r requirements.txt`

### Run test with sample data and output to matplotlib
`python path_tests.py`

