class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        N = len(locations)

        @lru_cache(None)
        def dp(curr, fuelLeft):
            ans = int(curr == finish)

            for nxt in range(N):
                if nxt != curr:
                    f = abs(locations[nxt] - locations[curr])

                    if f <= fuelLeft:
                        ans = (ans + dp(nxt, fuelLeft - f)) % MOD

            return ans

        return dp(start, fuel)
