from functools import lru_cache

MODULO = 10**9 + 7


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(maxsize=None)
        def dp(start_pos, fuel_remaining):
            if fuel_remaining < 0:
                return 0

            ways = 1 if start_pos == finish else 0

            if fuel_remaining == 0:
                return ways

            for i in range(len(locations)):
                if i == start_pos:
                    continue

                fuel_wasted = abs(locations[i] - locations[start_pos])
                ways = (ways + dp(i, fuel_remaining - fuel_wasted)) % MODULO

            return ways

        return dp(start, fuel)

