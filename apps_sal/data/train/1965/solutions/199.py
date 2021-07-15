from typing import *
from copy import deepcopy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x:(-x[0]))
        num_used = 0
        uf = [[i for i in range(n)]] + [[0] * n]
        i = 0
        while i < len(edges):
            t, s, d = edges[i]
            s -= 1
            d -= 1
            if t < 3:
                break
            i += 1
            if self.union_find_merge(uf, s, d):
                num_used += 1
        uf1 = deepcopy(uf)
        uf2 = deepcopy(uf)

        while i < len(edges):
            t, s, d = edges[i]
            s -= 1
            d -= 1
            if t < 2:
                break
            i += 1
            if self.union_find_merge(uf2, s, d):
                num_used += 1

        while i < len(edges):
            t, s, d = edges[i]
            s -= 1
            d -= 1
            i += 1
            if self.union_find_merge(uf1, s, d):
                num_used += 1

        if self.find_num_components(n, uf1) > 1 or self.find_num_components(n, uf2) > 1:
            return -1

        return len(edges) - num_used

    def find_num_components(self, n, uf):
        num_components = 0
        for idx in range(n):
            parent = uf[0][idx]
            if idx == parent:
                num_components += 1
        return num_components

    def union_find_merge(self, uf, node1, node2):
        p1 = self.union_find_get_parent(uf, node1)
        p2 = self.union_find_get_parent(uf, node2)

        if p1 == p2:
            return False  # Returning false so that we don't include the s,d in result

        if uf[1][p1] > uf[1][p2]:
            uf[0][p2] = p1
        else:
            uf[0][p1] = p2
            uf[1][p2] = max(uf[1][p2], uf[1][p1] + 1)

        return True

    def union_find_get_parent(self, uf, node):
        while uf[0][node] != node:
            node = uf[0][node]
        return node
