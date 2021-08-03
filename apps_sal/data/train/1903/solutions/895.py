class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i, p1 in enumerate(points):
            for j in range(i, len(points)):
                p2 = points[j]

                d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append([d, i, j])
        edges = sorted(edges)

        u = {i: i for i in range(n)}

        def head(i):
            if u[i] == i:
                return i
            else:
                h = head(u[i])
                u[i] = h
                return h

        def union(i, j):
            u[head(j)] = head(i)

        r = 0
        for d, i, j in edges:
            hi, hj = head(i), head(j)
            if hi != hj:
                r += d
                union(hi, hj)

        return r
