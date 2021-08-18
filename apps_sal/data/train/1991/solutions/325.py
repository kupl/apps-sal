class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        a = locations
        n = len(a)
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(pos, fuel):
            res = 0
            if pos == finish:
                res = 1
            for k in range(n):
                dist = abs(a[pos] - a[k])
                if dist > 0 and dist <= fuel:
                    res = (res + dp(k, fuel - dist)) % MOD
            return res

        return dp(start, fuel)
