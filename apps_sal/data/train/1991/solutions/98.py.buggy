class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        import sys
        sys.setrecursionlimit(10**9)
\t\t
        M = 10**9+7
        @lru_cache(None)
        def helper(curr_city, curr_fuel):
            if curr_fuel<0:
                return 0 
            
            ans = 0
            if curr_city==finish:
                ans += 1
            
            for i in range(len(locations)):
                if i!=curr_city:
                    ans += helper(i, curr_fuel - abs(locations[i]-locations[curr_city]))
                    ans %= M
            
            return ans
        
        return helper(start, fuel)
        
