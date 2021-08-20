class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def calculate_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        n = len(points)
        visited = set()
        res = 0
        m = 0
        dp = [sys.maxsize for _ in range(n)]
        for i in range(n - 1):
            (x, y) = points[m]
            visited.add(m)
            for j in range(n):
                if j in visited:
                    continue
                (x1, y1) = points[j]
                dp[j] = min(dp[j], calculate_distance(x, y, x1, y1))
            (v, m) = min(((j, i) for (i, j) in enumerate(dp)))
            dp[m] = sys.maxsize
            res += v
        return res
