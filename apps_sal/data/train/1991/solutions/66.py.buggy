from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        \"\"\"
        @lru_cache(None)
        def dp(i, fuel):
            if fuel < 0: return
            
            if i == finish:
                self.ans += 1
                
            for k, v in enumerate(locations):
                if k != i:
                    dp(k, fuel - abs(v - locations[i]))
                
            
        self.ans = 0
        dp(start, fuel)
        return self.ans % (10**9 + 7)
        \"\"\"
        
        
        @lru_cache(None)
        def dp(i, fuel):
            if fuel < 0: return 0
            
            res = 0
            if i == finish:
                res += 1
                
            res += sum(dp(k, fuel - abs(v - locations[i])) for k, v in enumerate(locations) if k != i)
            
            return res
        
        return dp(start, fuel) % (10**9 + 7)
        
