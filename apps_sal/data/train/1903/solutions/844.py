import heapq


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class UnionFind:

    def __init__(self, n):
        self.parents = list(range(n))

    def root(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.parents[self.root(x)] = self.root(y)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(q, (dist(points[i], points[j]), i, j))
        cost = 0
        s = UnionFind(len(points))
        while q:
            (d, i, j) = heapq.heappop(q)
            if s.root(i) != s.root(j):
                s.union(i, j)
                cost += d
        return cost
