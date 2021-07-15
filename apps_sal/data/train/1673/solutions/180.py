class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[-1][i] = A[-1][i]
        for i in range(n-2,-1,-1):
            for j in range(n):
                dp[i][j] = A[i][j] + min(dp[i+1][:j]+dp[i+1][j+1:])
        return min(dp[0])
