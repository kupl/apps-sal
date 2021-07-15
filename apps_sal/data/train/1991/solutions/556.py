class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        
        @lru_cache(None)
        def dfs(i, f):
            ans = (i == finish)
            for j in range(len(locations)):
                if j != i:
                    dist = abs(locations[i] - locations[j])
                    if f >= dist:
                        ans += dfs(j, f - dist) % mod
            return ans % mod
        
        return dfs(start, fuel)
