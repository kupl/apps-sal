class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        
        def dp(cur, fuel):
            if fuel < 0:
                return 0
            
            if (cur, fuel) in memo:
                return memo[(cur, fuel)]
            
            ans = 0
            
            if cur == locations[finish]:
                ans = 1
          
            for loc in locations:
                if loc != cur:
                    ans += dp(loc, fuel - abs(cur-loc))
            
            memo[(cur, fuel)] = ans 
            
            return ans
    
        memo = {}
        
        return dp(locations[start], fuel) % mod

