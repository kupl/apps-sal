class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(e1, e2):
            return abs(e1[0] - e2[0]) + abs(e1[1] - e2[1])

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            p[px] = py
            return True

        n = len(points)
        res = 0
        p = list(range(len(points)))
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                heappush(edges, (dist(points[i], points[j]), i, j))

        while edges:
            cost, x, y = heappop(edges)
            if union(x, y):
                res += cost

        return res
