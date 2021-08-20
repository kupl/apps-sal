class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        numCity = len(locations)
        dp = [[None] * numCity for _ in range(fuel + 1)]

        def helper(city, fuel):
            if fuel < 0:
                return 0
            res = dp[fuel][city]
            if res is not None:
                return res
            res = (int(city == finish) + sum((helper(city2, fuel - abs(locations[city] - locations[city2])) for city2 in range(numCity) if city != city2))) % (10 ** 9 + 7)
            dp[fuel][city] = res
            return res
        return helper(start, fuel)
