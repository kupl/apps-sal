class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1 for i in range(fuel + 1)] for j in range(len(locations))]
        for i in range(len(locations)):
            if i == finish:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        self.dfs(locations, start, fuel, finish, dp)
        return dp[start][fuel] % (10 ** 9 + 7)

    def dfs(self, locations, loc, fuel, finish, dp):
        if dp[loc][fuel] != -1:
            return
        if loc == finish:
            dp[loc][fuel] = 1
        else:
            dp[loc][fuel] = 0
        for next_loc in range(len(locations)):
            if next_loc == loc:
                continue
            if fuel >= abs(locations[loc] - locations[next_loc]):
                fuel_res = fuel - abs(locations[loc] - locations[next_loc])
                self.dfs(locations, next_loc, fuel_res, finish, dp)
                dp[loc][fuel] += dp[next_loc][fuel_res]
