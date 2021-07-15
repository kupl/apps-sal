from functools import lru_cache

class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(u, f):
            # Number of routes to finish from city u, with f fuel
            ans = +(u == finish)
            du = locations[u]
            for v, dv in enumerate(locations):
                if v != u:
                    delta = abs(du - dv)
                    if delta <= f:
                        ans += dp(v, f - delta)
                        ans %= MOD
            return ans
        
        return dp(start, fuel)
