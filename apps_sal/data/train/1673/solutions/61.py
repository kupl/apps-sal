class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        (m, n) = (len(arr), len(arr[0]))
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0] = arr[0]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min([dp[i - 1][col] for col in range(n) if col != j]) + arr[i][j]
        return min(dp[-1])
