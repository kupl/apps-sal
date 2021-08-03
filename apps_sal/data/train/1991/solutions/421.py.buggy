class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        numCity = len(locations)
        dp = [[None]*(fuel+1) for _ in range(numCity)]
        def helper(city, fuel):
            if fuel < 0: return 0
            res = dp[city][fuel]
            if res is not None: return res
            res = (int(city==finish) + sum(helper(city2, fuel-abs(locations[city]-locations[city2])) for city2 in range(numCity) if city!=city2)) % (10**9 + 7)
            dp[city][fuel] = res
            return res
        ans = helper(start, fuel)
        # print('\
'.join(map(str, dp)))
        return ans
