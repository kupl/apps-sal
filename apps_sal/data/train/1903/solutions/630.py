class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        parent = [x for x in range(N)]

        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]

        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            parent[ux] = uy

        def dist(a, b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])
        for i in range(N):
            for j in range(i + 1, N):
                edges.append((dist(i, j), i, j))
        edges.sort()
        total = 0
        for (cost, x, y) in edges:
            if ufind(x) != ufind(y):
                uunion(x, y)
                total += cost
        return total
