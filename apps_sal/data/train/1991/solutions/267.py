class Solution:
    def countRoutes(self, locations, start, finish, fuel):
        n = len(locations)
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(i, k):
            return (i == finish) + sum(dp(j, k - abs(locations[i] - locations[j])) for j in range(n) if i != j) % MOD if k >= 0 else 0
                
        return dp(start, fuel)
