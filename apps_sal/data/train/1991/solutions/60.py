from functools import lru_cache


class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(curr, fuel):
            if fuel < 0:
                return 0
            res = 1 if curr == finish else 0
            for (i, loc) in enumerate(locations):
                if i == curr:
                    continue
                fuel_used = abs(loc - locations[curr])
                res += dfs(i, fuel - fuel_used)
            return res % MOD
        res = dfs(start, fuel)
        return res % MOD
