from functools import lru_cache

class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        \"\"\"
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        \"\"\"
        
        M = 10**9 + 7
        n = len(locations)
        
        @lru_cache(None)
        def ways(city_idx, fuel_left):
            if fuel_left < 0 or abs(locations[city_idx] - locations[finish]) > fuel_left:
                return 0
            
            temp = 0
            
            if city_idx == finish:
                temp += 1
            
            for other_city in range(n):
                if other_city == city_idx:
                    continue
                cost = abs(locations[other_city] - locations[city_idx])
                new_fuel_left = fuel_left - cost
                temp += ways(other_city, new_fuel_left)
            
            return temp
                                       
        return ways(start, fuel) % M
        
        
