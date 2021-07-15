class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(None)
        def dp(cur, fuel) :
            if fuel == 0 and cur == start:
                return 1
            
            if fuel <=0:
                return 0
            ways = cur == start
            
            for i in range(len(locations)):
                if i !=cur :
                    ways += dp(i,   fuel -  abs(locations[i] - locations[cur]))
            return ways % (10**9+7)
        
        return dp(finish, fuel)
        

