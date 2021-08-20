class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = [i for i in range(n)]

        def union(a, b):
            (a, b) = (find(a), find(b))
            uf[a] = b

        def find(a):
            if uf[a] != a:
                uf[a] = find(uf[a])
            return uf[a]
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges = sorted(edges)
        c = 0
        for (a, x, y) in edges:
            if find(x) != find(y):
                c += a
                union(x, y)
        return c
