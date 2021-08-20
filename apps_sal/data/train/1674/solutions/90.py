from collections import defaultdict


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        dp = defaultdict(int)
        M = 1
        return self.DP(N, dp, piles, M, 0)

    def DP(self, n, dp, piles, M, start):
        if n <= 2 * M:
            return sum(piles[start:])
        if (n, M) in dp:
            return dp[n, M]
        res = float('-inf')
        for x in range(1, 2 * M + 1):
            newM = max(x, M)
            if n - x <= 2 * newM:
                res2 = 0
            else:
                res2 = float('inf')
                for y in range(1, 2 * newM + 1):
                    newM2 = max(y, newM)
                    res2 = min(res2, self.DP(n - x - y, dp, piles, newM2, start + x + y))
            res = max(res, res2 + sum(piles[start:start + x]))
        dp[n, M] = res
        return dp[n, M]
