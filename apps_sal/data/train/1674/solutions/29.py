import numpy as np
from functools import lru_cache


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        cumsum = np.cumsum(piles[::-1])

        @lru_cache(None)
        def optimalValue(m, s):
            if s == 0:
                return 0
            cumsum[s - 1]
            return max([cumsum[s - 1] - optimalValue(max(m, n), s - n) for n in range(1, 2 * m + 1) if s - n >= 0])
        return optimalValue(1, len(piles))
