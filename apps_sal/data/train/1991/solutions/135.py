class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)

        @lru_cache(None)
        def dp(i, fuel):
            if fuel < 0:
                return 0

            return int(i == finish) + sum(dp(k, fuel - abs(locations[i] - locations[k]))
                                          for k in range(N)
                                          if k != i) % (10**9 + 7)

        return dp(start, fuel)
