class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        numCity = len(locations)
        dp = [[None]*numCity for _ in range(fuel+1)] # row=fuel, col=city
        def helper(city, fuel):
            if fuel < 0: return 0
            res = dp[fuel][city]
            if res is not None: return res
            res = (int(city==finish) + sum(helper(city2, fuel-abs(locations[city]-locations[city2])) for city2 in range(numCity) if city!=city2)) % (10**9 + 7)
            dp[fuel][city] = res
            return res
        return helper(start, fuel)
                    
        # mod = 10**9 + 7
        # for city in range(numCity):
        #     dp[0][city] = 1 if city==finish else 0
        # for fuelLeft in range(1,fuel):
        #     for city in range(numCity):
        #         dist = lambda city1, city2: abs(locations[city1]-locations[city2])
        #         cost = lambda city2: dp[fuelLeft-dist(city,city2)][city2] if city!=city2 and dist(city,city2)<=fuelLeft else 0
        #         dp[fuelLeft][city] = (int(city==finish) + sum(map(cost, range(numCity)))) % mod
        # return sum(map)

