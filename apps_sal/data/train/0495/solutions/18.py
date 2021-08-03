from functools import lru_cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        lim = len(stones)

        @lru_cache(None)
        def r(s, i):
            if i == lim - 1:
                return min(s + stones[-1], abs(s - stones[-1]))

            else:

                return min(r(s + stones[i], i + 1), r(abs(s - stones[i]), i + 1))

        return r(0, 0)
