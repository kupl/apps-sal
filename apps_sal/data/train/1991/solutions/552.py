class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(u, f):
            ans = 1 if u == finish else 0
            du = locations[u]
            for (v, dv) in enumerate(locations):
                if u != v:
                    delta = abs(du - dv)
                    if delta <= f:
                        ans += dp(v, f - delta)
                        ans = ans % MOD
            return ans
        return dp(start, fuel)
