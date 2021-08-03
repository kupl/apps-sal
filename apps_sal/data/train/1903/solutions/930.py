class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):

                edges.append([distance(points[i], points[j]), i, j])

        edges.sort()

        p = [i for i in range(n)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return True

            else:
                p[px] = p[py]
        res = 0
        for edge in edges:
            d, x, y = edge
            if union(x, y):
                continue
            else:
                res += d
        return res
