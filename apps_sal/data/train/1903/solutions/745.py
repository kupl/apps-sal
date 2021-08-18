class DSU:
    def __init__(self, n):
        self.par = [x for x in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        self.par[yp] = xp
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        def dist(a, b, c, d): return abs(a - c) + abs(b - d)
        for i, p1 in enumerate(points):
            for j in range(i + 1, n):
                if (i == j):
                    continue
                p2 = points[j]
                edges.append([dist(*p1, *p2), i, j])

        def MST():
            res = 0
            dsu = DSU(n)
            for weight, p1, p2 in sorted(edges):
                if dsu.union(p1, p2):
                    res += weight
            return res

        return MST()
