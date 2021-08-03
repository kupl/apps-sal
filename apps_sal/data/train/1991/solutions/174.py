from functools import lru_cache
from collections import defaultdict


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cost = defaultdict(list)
        for i, c1 in enumerate(locations):
            for c2 in locations:
                cost[i].append(abs(c1 - c2))

        @lru_cache(None)
        def dp(position, f):
            ret = 0 if position != finish else 1
            for dst, c in enumerate(cost[position]):
                if f >= c and dst != position:
                    ret = (ret + dp(dst, f - c)) % 1000000007
            return ret
        return dp(start, fuel)
