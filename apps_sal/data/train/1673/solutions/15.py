class Solution:
    def minFallingPathSum(self, dp: List[List[int]]) -> int:
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i-1][:j]+dp[i-1][j+1:]) + dp[i][j]

        return min(dp[-1])
