class UnionFind:

    def __init__(self, n):
        self.leaders = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]

    def find(self, x):
        if self.leaders[x] != x:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return False
        if self.ranks[p] < self.ranks[q]:
            self.leaders[p] = q
        elif self.ranks[p] > self.ranks[q]:
            self.leaders[q] = p
        else:
            self.leaders[q] = p
            self.ranks[p] += 1
        return True


class Solution:

    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 1:
            return 0
        edges = []

        def dist(p0, p1):
            return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])
        for u in range(n):
            for v in range(u + 1, n):
                w = dist(points[u], points[v])
                edges.append([u, v, w])
        (res, cnt) = (0, 0)
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n + 1)
        for (u, v, w) in edges:
            if uf.union(u, v):
                res += w
                cnt += 1
            if cnt == n - 1:
                return res
