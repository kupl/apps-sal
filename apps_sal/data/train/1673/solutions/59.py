class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        dp = [[0] * n for i in range(m)]
        for j in range(n):
            dp[0][j] = arr[0][j]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min([dp[i - 1][k] for k in range(n) if k != j]) + arr[i][j]
        return min(dp[m - 1])
