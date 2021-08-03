class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        n = len(locations)

        @functools.lru_cache(None)
        def dp(i, f):
            if f < 0:
                return 0
            ans = sum(dp(j, f - abs(locations[i] - locations[j])) for j in range(n) if j != i)
            ans += i == finish
            return ans % mod
        return dp(start, fuel)
