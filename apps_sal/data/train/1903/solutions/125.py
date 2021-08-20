class DSU:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, i):
        if self.p[i] == i:
            return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        self.p[x] = y
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def w(u, v):
            return sum((abs(points[u][i] - points[v][i]) for i in range(2)))
        edges = [(u, v, w(u, v)) for u in range(n) for v in range(n)]
        edges.sort(key=lambda x: x[-1])
        ans = 0
        dsu = DSU(n)
        return sum((cost for [u, v, cost] in edges if dsu.unite(u, v)))
