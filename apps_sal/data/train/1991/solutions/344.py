# O(f ^ 2 * n ^ 2), f is fuel, n is number of cities
from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def ways(left, city):
            # it's not possible that we have more than initial fuel
            if left > fuel: return 0
            if city == locations[start] and left == fuel: return 1
            return sum(ways(abs(city - city_) + left, city_) for city_ in locations if city != city_) % MOD
            
        return sum(ways(left, locations[finish]) for left in range(fuel + 1)) % MOD
        # AC: 4388 ms, beats 23.53%, 47.6 MB, beats 5.14%
                
                    

