class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(f, fuel):
            if fuel < 0:
                return 0
            ans = 0
            if f == finish:
                ans = 1
            for t in range(0, n):
                if t != f:
                    ans += dp(t, fuel - abs(locations[f] - locations[t]))
                    ans %= MOD
            return ans
        return dp(start, fuel)
