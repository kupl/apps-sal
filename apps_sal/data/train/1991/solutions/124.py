class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        n = len(locations)
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(used, node):
                if used > fuel: return 0
                res = 1 if node == finish else 0
                    
                for nxt in range(n):
                    if node == nxt: continue
                    nused = used + abs(locations[node] - locations[nxt])
                    res += dp(nused, nxt) % MOD
                return res
            
            
        return dp(0, start) % MOD
