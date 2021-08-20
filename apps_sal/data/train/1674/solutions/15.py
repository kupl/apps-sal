class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        m = len(piles)
        dp = [[0 for j in range(m + 1)] for i in range(m)]
        sumv = 0
        for i in range(m - 1, -1, -1):
            sumv += piles[i]
            for M in range(1, len(dp[0])):
                if 2 * M + i >= m:
                    dp[i][M] = sumv
                else:
                    for x in range(1, 2 * M + 1):
                        dp[i][M] = max(dp[i][M], sumv - dp[i + x][max(M, x)])
        return dp[0][1]
