from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def td_solve(gas, s):
            if gas < abs(locations[s] - locations[finish]):
                return 0

            res = 1 if s == finish else 0
            for city in range(len(locations)):
                if city == s:
                    continue

                res += td_solve(gas - abs(locations[city] - locations[s]),
                                city)
                res %= MOD

            return res

        return td_solve(fuel, start)
