class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dp[i][j] = dp[j][i] = w
        for i in range(n):
            dp[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        min_idx, min_val = None, None
        for i in range(n):
            can_val = sum(v <= distanceThreshold for v in dp[i])
            if min_val is None or can_val <= min_val:
                min_val = can_val
                min_idx = i
        return min_idx
