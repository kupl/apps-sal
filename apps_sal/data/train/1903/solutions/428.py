class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            idx = find(x)
            idy = find(y)
            if idx == idy:
                return
            uf[idy] = idx

        def dist(x, y):
            return abs(y[0] - x[0]) + abs(y[1] - x[1])
        n = len(points)
        uf = {i: i for i in range(n)}
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                a = points[i]
                b = points[j]
                edges.append((i, j, dist(a, b)))
        edges = sorted(edges, key=lambda x: x[2])
        cost = 0
        for edge in edges:
            x = edge[0]
            y = edge[1]
            if find(x) != find(y):
                union(x, y)
                cost += edge[2]
        return cost
