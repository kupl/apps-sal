class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[0][i] = arr[0][i]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1:]) + arr[i][0]
            for j in range(1, n - 1):
                minLeft = min(dp[i - 1][:j])
                minRight = min(dp[i - 1][(j + 1):])
                dp[i][j] = min(minLeft, minRight) + arr[i][j]
            dp[i][-1] = min(dp[i - 1][:(-1)]) + arr[i][-1]
        return min(dp[-1])
