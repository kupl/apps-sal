class DSU:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.par[px] = py


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        def dist(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)
        lens = []
        res = 0
        n = len(points)
        dsu = DSU(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                lens.append((dist(points[i][0], points[i][1], points[j][0], points[j][1]), i, j))
        heapq.heapify(lens)
        while lens:
            dist, i, j = heapq.heappop(lens)
            if dsu.find(i) != dsu.find(j):
                dsu.union(i, j)
                res += dist
        return res
