class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def step(loc, fuel_left):
            if fuel_left < 0:
                return 0
            
            ans = int(loc == locations[finish])
            for dest in locations:
                if dest != loc:
                    ans = (ans + step(dest, fuel_left - abs(dest - loc))) % (10 ** 9 + 7)
            return ans
        
        return step(locations[start], fuel)
