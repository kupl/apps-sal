class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float(inf)] * n for _ in range(n)]

        for a, b, cost in edges:
            dp[a][b] = cost
            dp[b][a] = cost

        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        idx = 0
        m = len([e for e in dp[0] if e <= distanceThreshold])
        for i in range(1, n):
            l = len([e for e in dp[i] if e <= distanceThreshold])
            if l <= m:
                m = l
                idx = i
        return idx
