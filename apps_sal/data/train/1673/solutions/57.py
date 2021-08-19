class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = arr[:]
        (m, n) = (len(arr), len(arr[0]))
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = arr[i][j] + min((dp[i - 1][k] for k in range(n) if k != j))
        return min(dp[-1])
