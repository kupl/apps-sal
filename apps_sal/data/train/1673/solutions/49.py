class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[float('inf')] + i + [float('inf')] for i in arr]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])-1):
                dp[i][j] = dp[i][j] + min([dp[i-1][k] for k in range(len(dp[i-1])) if k != j])
                
        return min(dp[-1])
