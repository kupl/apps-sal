from typing import List


class DS:

    def __init__(self, n):
        self.sizes = [1] * n
        self.roots = list(range(n))

    def find(self, v):
        root = v
        while root != self.roots[root]:
            self.roots[root] = self.roots[self.roots[root]]
            root = self.roots[root]
        return root

    def union(self, u, v):
        (root_u, root_v) = (self.find(u), self.find(v))
        if root_u != root_v:
            (s_root, l_root) = (root_u, root_v) if self.sizes[root_u] < self.sizes[root_v] else (root_v, root_u)
            self.roots[s_root] = l_root
            self.sizes[l_root] += self.sizes[s_root]

    def connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ds = DS(len(points))

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        sorted_edges = sorted(((dist(i, j), i, j) for i in range(len(points)) for j in range(i + 1, len(points))))
        cost = 0
        for (d, u, v) in sorted_edges:
            if not ds.connected(u, v):
                ds.union(u, v)
                cost += d
        return cost
