from heapq import heapify, heappop


class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.rank = 0
        self.size = 1
        self.value = value


class UnionFind:
    def __init__(self, nodes):
        self.subsets = [Node(i, v) for i, v in enumerate(nodes)]
        self.maxSubsetSize = 1

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        # union by rank
        if self.subsets[irep].rank > self.subsets[jrep].rank:
            self.subsets[jrep].parent = irep
            self.subsets[irep].size += self.subsets[jrep].size
        elif self.subsets[jrep].rank > self.subsets[irep].rank:
            self.subsets[irep].parent = jrep
            self.subsets[jrep].size += self.subsets[irep].size
        else:
            self.subsets[irep].parent = jrep
            self.subsets[jrep].rank += 1
            self.subsets[jrep].size += self.subsets[irep].size
        self.maxSubsetSize = max(self.maxSubsetSize, max(self.subsets[irep].size, self.subsets[jrep].size))

    def find(self, i):
        if self.subsets[i].parent != i:
            # path compression
            self.subsets[i].parent = self.find(self.subsets[i].parent)
        return self.subsets[i].parent


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points), 1):
                x2, y2 = points[j]
                edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))
        heapify(edges)
        uf = UnionFind(range(len(points)))
        total = 0
        while len(edges) > 0:
            d, i, j = heappop(edges)
            if uf.find(i) != uf.find(j):
                total += d
                uf.union(i, j)
        return total
