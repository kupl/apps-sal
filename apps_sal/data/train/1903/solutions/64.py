class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, x, y):
        (rx, ry) = (self.find(x), self.find(y))
        self.p[rx] = ry


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        hq = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(hq, (dist, i, j))
        connect = 0
        uf = UnionFind(len(points))
        cost = 0
        while connect != len(points) - 1 and hq:
            (d, i, j) = heapq.heappop(hq)
            (ri, rj) = (uf.find(i), uf.find(j))
            if ri != rj:
                cost += d
                uf.union(i, j)
        return cost
