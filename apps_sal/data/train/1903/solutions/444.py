class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def md(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        q = [md(points[0], p) for p in points]
        print(q)
        res = 0
        for _ in range(len(points) - 1):
            d, j = min((d, j) for j, d in enumerate(q) if d > 0)
            print((d, j))
            res += d
            q = [min(q[i], md(points[i], points[j])) for i in range(len(q))]
        return res

