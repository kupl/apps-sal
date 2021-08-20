class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]
        ans = self.dfs(locations, start, finish, fuel, dp)
        return ans

    def dfs(self, location, curr_city, finish, fuel, dp):
        if fuel < 0:
            return 0
        if dp[curr_city][fuel] != -1:
            return dp[curr_city][fuel]
        ans = 0
        if curr_city == finish:
            ans = 1
        for next_city in range(len(location)):
            if next_city == curr_city:
                continue
            else:
                ans = ans + self.dfs(location, next_city, finish, fuel - abs(location[curr_city] - location[next_city]), dp)
                ans %= 1000000007
        dp[curr_city][fuel] = ans
        return ans
