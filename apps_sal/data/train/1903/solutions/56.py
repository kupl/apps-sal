class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        edges = []
        N = len(points)
        parent = [x for x in range(N)]

        def ufind(x):
            if parent[x] != x:
                return ufind(parent[x])
            return x

        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            parent[uy] = ux

        def dist(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)
        for i in range(N):
            (xi, yi) = points[i]
            for j in range(i + 1, N):
                (xj, yj) = points[j]
                edges.append((dist(xi, yi, xj, yj), i, j))
        edges.sort()
        for (edge, i, j) in edges:
            if ufind(i) != ufind(j):
                uunion(i, j)
                total += edge
        return total
