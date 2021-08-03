class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(cur, fuel):
            if fuel < 0:
                return 0
            ret = 1 if cur == finish else 0
            for i in range(len(locations)):
                if i == cur:
                    continue
                ret += dp(i, fuel - abs(locations[i] - locations[cur]))
            return ret % MOD

        return dp(start, fuel)
