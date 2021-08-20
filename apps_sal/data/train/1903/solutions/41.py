class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dis(x, y, x1, y1):
            return abs(x - x1) + abs(y - y1)
        distances = []
        for (i, (x, y)) in enumerate(points):
            for (x1, y1) in points[i + 1:]:
                d = dis(x, y, x1, y1)
                distances.append((d, x, y, x1, y1))
        uf = UnionFind(len(points))
        for (x, y) in points:
            uf.parents[x, y] = (x, y)
        distances.sort()
        ans = 0
        for (d, x, y, x1, y1) in distances:
            if uf.union((x, y), (x1, y1)):
                ans += d
        return ans


class UnionFind:

    def __init__(self, n):
        self.component_count = n
        self.parents = {}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return False
        self.parents[y0] = x0
        return True
