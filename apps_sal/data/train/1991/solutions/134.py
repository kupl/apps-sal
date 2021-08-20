class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1] * (fuel + 1) for _ in range(len(locations))]

        def route(st, ed, fuel):
            if dp[st][fuel] > -1:
                return dp[st][fuel]
            res = 0 if st != ed else 1
            for i in range(len(locations)):
                if i != st and fuel - abs(locations[st] - locations[i]) >= 0:
                    res += route(i, ed, fuel - abs(locations[st] - locations[i]))
            dp[st][fuel] = res % 1000000007
            return dp[st][fuel]
        return route(start, finish, fuel)
