class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def help(locations, cur, e, dp, fuel):
            if fuel < 0:
                return 0
            if dp[cur][fuel] != -1:
                return dp[cur][fuel]
            ans = 1 if cur == e else 0
            for next in range(len(locations)):
                if next != cur:
                    ans = (ans + help(locations, next, e, dp, fuel - abs(locations[cur] - locations[next]))) % 1000000007

            dp[cur][fuel] = ans
            return ans

        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        return help(locations, start, finish, dp, fuel)
