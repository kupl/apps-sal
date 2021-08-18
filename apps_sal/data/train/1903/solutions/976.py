class UnionFind:
    def __init__(self, V):
        self.parent = [-1] * V

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 == r2:
            return

        s1 = self.size(r1)
        s2 = self.size(r2)

        if s1 <= s2:
            self.parent[r1] = r2
            self.parent[r2] -= s1
        else:
            self.parent[r2] = r1
            self.parent[r1] -= s2

    def find(self, v):
        r = v
        while self.parent[r] >= 0:
            r = self.parent[r]

        while v != r:
            new_v = self.parent[v]
            self.parent[v] = r
            v = new_v

        return r

    def size(self, v):
        r = self.find(v)
        s = -self.parent[r]
        return s


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for u in range(n):
            for v in range(u + 1, n):
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                edges.append([dist, u, v])

        res = 0
        uf = UnionFind(n)
        for e in sorted(edges):
            if uf.find(e[1]) != uf.find(e[2]):
                res += e[0]
                uf.union(e[1], e[2])
        return res
