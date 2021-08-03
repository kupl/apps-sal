from typing import *
from collections import defaultdict
import heapq


class BreakIt(Exception):
    pass


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        G = self.construct_graph(edges)
        # start from n --> 1, keep a track of smallest num of neighbours, prempt if some node has more than smallest num of neighbours found so far
        smallest_neigh_count = float(\"inf\")
        smallest_neigh_node = None
        for i in range(n - 1, -1, -1):
            valid_n = set()
            q = []
            heapq.heappush(q, (0, i))
            visited = set()
            shortest_distance_i = dict()
            try:
                while len(q) > 0:
                    d, curr_n = heapq.heappop(q)
                    visited.add(curr_n)
                    for n, nd in G[curr_n]:
                        old_d = self.relax_distance(shortest_distance_i, n, d + nd)
                        found_shorter_path = old_d > d + nd
                        if d + nd <= distanceThreshold and n != i:
                            valid_n.add(n)
                        if len(valid_n) >= smallest_neigh_count:
                            raise BreakIt
                        if n not in visited or found_shorter_path:
                            heapq.heappush(q, (d + nd, n))
                if len(valid_n) < smallest_neigh_count:
                    smallest_neigh_count = len(valid_n)
                    smallest_neigh_node = i
            except BreakIt:
                pass
        return smallest_neigh_node

    @staticmethod
    def relax_distance(distance_map, d, dist):
        curr_d = distance_map.get(d, float(\"inf\"))
        if dist < curr_d:
            distance_map[d] = dist
        return curr_d

    @staticmethod
    def construct_graph(edges):
        G = defaultdict(set)
        for e in edges:
            n1, n2, w = e
            G[n1].add((n2, w))
            G[n2].add((n1, w))
        return G

