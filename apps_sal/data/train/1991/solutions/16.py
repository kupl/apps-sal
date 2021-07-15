class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def recurse(fuel, curr_city):
            if fuel == 0 and curr_city == finish:
                return 1
            if fuel == 0:
                return 0 
            
            array = []
            for index, city_val in enumerate(locations):
                if curr_city != index:
                    fuel_left = fuel - abs(locations[curr_city] - city_val)
                    if fuel_left >= 0:
                        array.append(recurse(fuel_left, index))
                        
            if curr_city != finish:
                return sum(array)
            else:
                return sum(array)+1
            
        return recurse(fuel,start) % (10**9 + 7)
