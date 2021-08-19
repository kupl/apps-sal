class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        # locations[start], locations[0] = locations[0], locations[start]
        # locations[finish], locations[n-1] = locations[n-1], locations[finish]
        # start = 0
        # finish = n - 1
        MOD = 10**9 + 7

        # print(locations)

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
