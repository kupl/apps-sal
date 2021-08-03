class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def helper(ind, curr):
            if ind == len(stones):
                return abs(curr)

            return min(helper(ind + 1, curr + stones[ind]), helper(ind + 1, curr - stones[ind]))

        return helper(0, 0)
