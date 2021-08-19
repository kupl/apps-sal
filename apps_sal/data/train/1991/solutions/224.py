class Solution:

    def dfs(self, cur, end, dp, locations, fuel):
        if fuel < 0:
            return 0
        if dp[cur][fuel] != -1:
            return dp[cur][fuel]
        if cur == end:
            ans = 1
        else:
            ans = 0
        for next_city in range(len(locations)):
            if next_city != cur:
                ans = (ans + self.dfs(next_city, end, dp, locations, fuel - abs(locations[next_city] - locations[cur]))) % 1000000007
        dp[cur][fuel] = ans
        return ans

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1 for _ in range(fuel + 1)] for _ in range(n)]
        return self.dfs(start, finish, dp, locations, fuel)
