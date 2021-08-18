

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        ds = [float('inf') for _ in range(n)]
        for i in range(1, n):
            ds[i] = dist(points[0], points[i])

        ans = 0
        for i in range(1, n):
            v = ds.index(min(ds))
            ans += ds[v]
            ds[v] = float('inf')
            for i in range(n):
                if ds[i] == float('inf'):
                    continue
                ds[i] = min(ds[i], dist(points[i], points[v]))

        return ans
