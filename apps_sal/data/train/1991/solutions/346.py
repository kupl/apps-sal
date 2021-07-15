class Solution:
    
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        
        @functools.lru_cache(maxsize=None)
        def helper(L, i, j, fuel):
            output = 0
            if fuel < 0:
                return output            
            if i == j and fuel >= 0:
                output = 1
                
            if fuel > 0:
                for k in range(len(locations)):
                    if i == k:
                        continue
                    output += helper(L, k, j, fuel-abs(locations[i]-locations[k]))
            return output

        
        return (helper(tuple(locations), start, finish, fuel))%(10**9+7)
                
            
            
            
        
            

