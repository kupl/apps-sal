class Solution:

    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        cols = len(cost[0])
        dp = cost[0]
        for h in range(1, len(cost)):
            prev = sorted(cost[h - 1])
            for m in range(0, cols):
                cost[h][m] += prev[1] if cost[h - 1][m] == prev[0] else prev[0]
        return min(cost[-1])
