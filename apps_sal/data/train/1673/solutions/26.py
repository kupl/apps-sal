class Solution:

    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        cols = len(cost[0])
        dp = cost[0]

        for h in range(1, len(cost)):
            dp = [cost[h][m] + min(dp[prevMat]
                                   for prevMat in range(0, cols)
                                   if prevMat != m)
                  for m in range(0, cols)]

        return min(dp)
