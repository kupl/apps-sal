from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def value(M, ind):
            if ind >= n:
                return 0

            v_max = 0
            for X in range(1, 2 * M + 1):
                M_new = max(X, M)
                v = sum(piles[ind:]) - value(M_new, ind + X)
                v_max = max(v, v_max)
            return v_max

        val = value(1, 0)
        return val
