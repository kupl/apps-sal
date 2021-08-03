class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        n = len(arr)

        dp = [([0] * n) for _ in range(n)]
        dp[0] = arr[0]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = arr[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])

        return min(dp[-1])
