class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dp(u, fuel):
            ans = +(u == finish)
            du = locations[u]
            for v, dv in enumerate(locations):
                if v != u:
                    delta = abs(du - dv)
                    if fuel - delta >= 0:
                        ans += dp(v, fuel - delta)
                        ans %= mod
            return ans
        return dp(start, fuel)
