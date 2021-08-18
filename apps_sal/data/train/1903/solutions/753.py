from sortedcontainers import SortedList


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ret, n = 0, len(points)

        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)

        def dis(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dis(points[i], points[j]), i, j))

        edges.sort()
        for cost, u, v in edges:
            if find(u) != find(v):
                ret += cost
                union(u, v)

        return ret
