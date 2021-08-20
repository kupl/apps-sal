class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        presum = list(piles)
        for i in range(1, len(piles)):
            presum[i] += presum[i - 1]
        from functools import lru_cache

        @lru_cache(None)
        def dp(ind, m):
            if ind + 2 * m >= len(piles):
                return presum[-1] - (presum[ind - 1] if ind > 0 else 0)
            sm = float('-inf')
            for i in range(1, 2 * m + 1):
                me = presum[ind + i - 1] - (presum[ind - 1] if ind > 0 else 0)
                sm = max(sm, me + presum[-1] - presum[ind + i - 1] - dp(ind + i, max(m, i)))
            return sm
        return dp(0, 1)
