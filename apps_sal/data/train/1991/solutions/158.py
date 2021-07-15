from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def h(start, finish, fuel):
            if fuel < 0:
                return 0
            res = start == finish
            for i in range(len(locations)):
                if i != start:
                    res += h(i, finish, fuel - abs(locations[i] - locations[start]))
            return res        
        
        return h(start, finish, fuel) % (10**9 + 7)
