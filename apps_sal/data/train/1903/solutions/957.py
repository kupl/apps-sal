import heapq


class DSU:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            self.p[p_x] = p_y
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([dist(points[i], points[j]), i, j])
        heapq.heapify(edges)
        dsu = DSU(n)
        res = 0
        while edges:
            (cost, p1, p2) = heapq.heappop(edges)
            if dsu.union(p1, p2):
                res += cost
        return res
