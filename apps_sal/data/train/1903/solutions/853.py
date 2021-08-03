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
        def manh(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        n, q = len(points), []

        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(q, (manh(points[i][0], points[j][0], points[i][1], points[j][1]), i, j))

        cost = 0

        s = UnionFind(n)
        while q:
            d, i, j = heapq.heappop(q)
            if s.root(i) != s.root(j):
                s.union(i, j)
                cost += d
        return cost
