from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dp(f, i):
            if (f, i) == (fuel, start): return 1
            ans = 0
            for j in range(n):
                if i == j: continue
                nd = f + abs(locations[j] - locations[i])
                if nd <= fuel:
                    ans = (ans + dp(nd, j)) % md
            return ans
        n, md = len(locations), 10**9+7
        res = 0
        for i in range(fuel+1):
            res = (res + dp(i, finish)) % md
        return res
