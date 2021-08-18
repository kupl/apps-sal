class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1] * (fuel) for _ in range(len(locations))]

        def route(st, ed, fuel):
            if fuel < 0:
                return 0
            if dp[st][fuel - 1] > -1:
                return dp[st][fuel - 1]
            res = 0 if st != ed else 1
            for i in range(len(locations)):
                if i != st:
                    res += route(i, ed, fuel - abs(locations[st] - locations[i]))
            dp[st][fuel - 1] = res % 1000000007
            return dp[st][fuel - 1]
        return route(start, finish, fuel)
