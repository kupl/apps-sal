class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(locations)
        
        @functools.lru_cache(None)
        def dfs(u, f):
            ans = 0
            if u == finish:
                ans += 1
            if f <= 0:
                return ans
            for v in range(N):
                if u == v:
                    continue
                cost = abs(locations[v] - locations[u])
                if cost <= f:
                    ans += dfs(v, f - cost) % MOD
            return ans
        
        return dfs(start, fuel) % MOD
