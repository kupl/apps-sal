class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        start_loc = locations[start]
        finish_loc = locations[finish]
        locations.sort()
        start = bisect_left(locations, start_loc)
        finish = bisect_left(locations, finish_loc)
        @lru_cache(None)
        def dp(cur, cur_fuel):
            total = 1 if cur == finish else 0
            if abs(locations[cur] - locations[finish]) > fuel:
                return 0
            for i in range(cur + 1, len(locations)):
                dist = locations[i] - locations[cur]
                if dist <= cur_fuel:
                    total += dp(i, cur_fuel - dist)
                else:
                    break
            
            for i in reversed(list(range(0, cur))):
                dist = locations[cur] - locations[i]
                if dist <= cur_fuel:
                    total += dp(i, cur_fuel - dist)
                else:
                    break
            
            return total
        
        return dp(start, fuel) % 1_000_000_007

