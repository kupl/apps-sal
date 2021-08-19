class UF:

    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]

    def unite(self, a, b):
        self.root[self.find(a)] = self.find(b)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        (edges, res) = ([], 0)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        edges.sort()
        uf = UF(n)
        for (w, s, t) in edges:
            if uf.find(s) != uf.find(t):
                uf.unite(s, t)
                res += w
        return res
