import sys
input = sys.stdin.readline


class Unionfind:

    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [1] * n

    def root(self, x):
        r = x
        while not self.par[r] < 0:
            r = self.par[r]
        t = x
        while t != r:
            tmp = t
            t = self.par[t]
            self.par[tmp] = r
        return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.rank[rx] <= self.rank[ry]:
            self.par[ry] += self.par[rx]
            self.par[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
        else:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return -self.par[self.root(x)]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            (xi, yi) = points[i]
            for j in range(i + 1, len(points)):
                (xj, yj) = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))
        edges.sort()
        uf = Unionfind(len(points))
        ans = 0
        for (w, u, v) in edges:
            if not uf.is_same(u, v):
                ans += w
                uf.unite(u, v)
        return ans
