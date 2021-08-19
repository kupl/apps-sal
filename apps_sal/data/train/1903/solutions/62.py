class DSU:

    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [1] * N

    def __find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.__find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.__find(x)
        y = self.__find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.parents[y] = x
        self.size[x] += self.size[y]
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        def kruskals(N, edges):
            cost = 0
            dsu = DSU(N)
            for (i, j, dist) in edges:
                if dsu.union(i, j):
                    cost += dist
            return cost
        for (i, (x, y)) in enumerate(points):
            for (j, (x1, y1)) in enumerate(points):
                if i != j:
                    dist = abs(x1 - x) + abs(y1 - y)
                    edges.append([i, j, dist])
        edges.sort(key=lambda v: v[2])
        return kruskals(len(points), edges)
