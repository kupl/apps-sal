import heapq
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[float('inf')] + i + [float('inf')] for i in arr]
        for i in range(1,len(dp)):
            hp = heapq.nsmallest(2, dp[i - 1])
            for j in range(1,len(dp[0])-1):
                dp[i][j] +=  hp[0] if dp[i-1][j] != hp[0] else hp[1]
        return min(dp[-1])
