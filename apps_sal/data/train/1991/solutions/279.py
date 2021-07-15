class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = (10**9) + 7

        dp = [[-1] * (len(locations) + 1)] * fuel

        @lru_cache(None)
        def routes(cur_city, fuel):
            nonlocal locations, dp

            if fuel < 0: return 0

            # if dp[cur_city][fuel] != -1: return dp[cur_city][fuel]
            
            total = 0

            if cur_city == finish: total += 1

            for i, val in enumerate(locations):
                if i != cur_city:
                    total += routes(i, fuel - abs(locations[i] - locations[cur_city])) % MOD
            
            # dp[cur_city][fuel] = total % MOD
            return total % MOD


        return routes(start, fuel)

