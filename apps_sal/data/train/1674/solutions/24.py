class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def dp1(prev, m):
            if prev >= n - 1:
                return 0
            maxcount = 0
            for x in range(1, m * 2 + 1):
                if prev + x >= n:
                    break
                ret = dp2(prev + x, max(m, x))
                maxcount = max(maxcount, ret + sum(piles[prev + 1:prev + x + 1]))
            return maxcount

        @lru_cache(None)
        def dp2(prev, m):
            if prev >= n - 1:
                return 0
            maxcount = float('inf')
            for x in range(1, m * 2 + 1):
                if prev + x >= n:
                    break
                ret = dp1(prev + x, max(m, x))
                maxcount = min(maxcount, ret)
            return maxcount
        return dp1(-1, 1)
