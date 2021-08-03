class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def step(loc, fuel_left):
            ans = int(loc == locations[finish])
            for dest in locations:
                new_fuel = fuel_left - abs(dest - loc)
                if dest != loc and new_fuel >= 0:
                    ans = (ans + step(dest, new_fuel)) % (10 ** 9 + 7)
            return ans

        return step(locations[start], fuel)
