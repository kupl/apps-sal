class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, f):
            ans = 0
            if i == finish:
                ans += 1
            for j, nex in enumerate(locations):
                if i != j and (used := abs(nex - locations[i])) <= f:
                    ans += dfs(j, f - used)
            return ans % MOD
        return dfs(start, fuel)
