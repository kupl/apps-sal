class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        MOD = 10 ** 9 + 7
        
        @functools.lru_cache(None)
        def dfs(u, k):
            ans = 0
            if u == finish:
                ans += 1
            if k < 1:
                return ans
            for v in range(N):
                if v == u:
                    continue
                cost = abs(locations[v] - locations[u])
                if cost > k:
                    continue
                ans += dfs(v, k - cost)
            return ans % MOD
        
        return dfs(start, fuel) % MOD
