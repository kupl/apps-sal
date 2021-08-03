class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(u):
            if p[u] == -1:
                return u

            p[u] = find(p[u])
            return p[u]

        def union(u, v):

            if r[u] > r[v]:
                p[v] = u
            elif r[u] < r[v]:
                p[u] = v
            else:
                p[v] = u
                r[u] += 1

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), i, j])

        edges.sort()

        p = [-1] * n
        r = [0] * n

        res = 0

        for x in edges:
            u = find(x[1])
            v = find(x[2])
            if u != v:
                res += x[0]
                union(u, v)

        return res
