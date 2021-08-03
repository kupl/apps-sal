class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] >= self.rank[py]:
            self.p[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.p[px] = py
            self.rank[py] += self.rank[px]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        uf = UnionFind(n)

        def dis(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        edges = sorted((dis(i, j), i, j) for i in range(n) for j in range(i + 1, n))
        connected = 0
        for d, i, j in edges:
            if connected == n:
                return res
            if uf.union(i, j):
                connected += 1
                res += d

        return res
