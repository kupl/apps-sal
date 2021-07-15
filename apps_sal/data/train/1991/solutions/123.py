class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        n = len(locations)
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(used, node):
                if used > fuel: return 0
                #到达了终点，要加一
                res = 1 if node == finish else 0
                
                #就算到达了终点也不能return，还得继续跑
                for nxt in range(n):
                    if node == nxt: continue
                    nused = used + abs(locations[node] - locations[nxt])
                    res += dp(nused, nxt) % MOD
                return res
            
        return dp(0, start) % MOD
