class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @functools.lru_cache(None)
        def dp(i, f):
            ans = 0 if i != finish else 1
            for j in range(n):
                if i == j:
                    continue
                ff = abs(locations[i] - locations[j])
                if f >= ff:
                    ans += dp(j, f - ff)
            return ans % (10 ** 9 + 7)
        return dp(start, fuel)
