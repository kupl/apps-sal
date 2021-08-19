from functools import lru_cache


class Solution:

    def stoneGameII(self, a: List[int]) -> int:
        n = len(a)
        sums = [0] * n
        sums[-1] = a[-1]
        for i in reversed(range(len(sums) - 1)):
            sums[i] = a[i] + sums[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0
            return max((sums[i] - dp(i + x, max(x, m)) for x in range(1, 2 * m + 1)))
        return dp(0, 1)
