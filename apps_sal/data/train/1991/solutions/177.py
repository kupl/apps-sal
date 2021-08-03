class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        return self.dfs(start, finish, fuel, dp, locations)

    def dfs(self, start, finish, fuel, dp, locations):
        if fuel < 0:
            return 0
        if dp[start][fuel] > -1:
            return dp[start][fuel]

        if start == finish:
            res = 1
        else:
            res = 0

        n = len(locations)
        for i in range(n):
            if i == start:
                continue
            else:
                res += self.dfs(i, finish, fuel - abs(locations[i] - locations[start]), dp, locations)

        dp[start][fuel] = res % (10 ** 9 + 7)

        return dp[start][fuel]
