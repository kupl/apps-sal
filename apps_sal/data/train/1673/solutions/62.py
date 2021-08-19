class Solution:

    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        cols = len(cost[0])
        dp = cost[0]
        for h in range(1, len(cost)):
            for m in range(0, cols):
                cost[h][m] += min((cost[h - 1][prevMat] for prevMat in range(0, cols) if prevMat != m))
        return min(cost[-1])
