import functools


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return piles[i]
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, piles[i] - dp(i + x, max(m, x)))
            return res
        return dp(0, 1)
