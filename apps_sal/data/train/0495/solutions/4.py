from functools import lru_cache


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]

        @lru_cache(None)
        def dfs(index, curSum):
            if index == n:
                return abs(curSum)
            return min(dfs(index + 1, curSum + stones[index]), dfs(index + 1, curSum - stones[index]))
        return dfs(0, 0)
