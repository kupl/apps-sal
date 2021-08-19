class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = pow(10, 9) + 7
        N = len(locations)

        @lru_cache(None)
        def dfs(cur, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if cur == finish:
                ans += 1
            for (i, loc) in enumerate(locations):
                if i == cur:
                    continue
                if fuel >= abs(locations[i] - locations[cur]):
                    ans += dfs(i, fuel - abs(locations[i] - locations[cur])) % MOD
                    ans %= MOD
            ans %= MOD
            return ans
        return dfs(start, fuel)
