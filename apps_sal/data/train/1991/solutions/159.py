class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(fuel_left, curr_loc):
            if fuel_left < 0:
                return 0
            ways = 0
            if fuel_left >= 0 and curr_loc == finish:
                ways = 1
            for i in range(len(locations)):
                if i != curr_loc:
                    ways += dp(fuel_left - abs(locations[curr_loc] - locations[i]), i) % MOD
            return ways % MOD
        return dp(fuel, start) % MOD
