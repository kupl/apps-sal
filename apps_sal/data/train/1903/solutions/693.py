class DSU:

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        (par_x, par_y) = (self.find(x), self.find(y))
        if par_x == par_y:
            return False
        if self.size[par_x] < self.size[par_y]:
            (par_x, par_y) = (par_y, par_x)
        self.parent[par_y] = par_x
        self.size[par_x] += self.size[par_y]
        self.size[par_y] = self.size[par_x]
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        N = len(points)
        if not points:
            return -1
        for i in range(N):
            for j in range(i + 1, N):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append([i, j, d])
        UF = DSU(N)
        total_cost = 0
        edges.sort(key=lambda x: x[2])
        for (i, j, d) in edges:
            if UF.union(i, j):
                total_cost += d
        return total_cost
