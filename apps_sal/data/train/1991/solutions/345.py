class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        self.mode = int(1000000000.0) + 7
        return self.dfs(fuel, start, finish, locations, dp)

    def dfs(self, fuel, u, target, locations, dp):
        if fuel < 0:
            return 0
        if (fuel, u, target) in dp:
            return dp[fuel, u, target]
        ans = 1 if u == target else 0
        for v in range(len(locations)):
            if u == v:
                continue
            ans += self.dfs(fuel - abs(locations[u] - locations[v]), v, target, locations, dp)
            ans %= self.mode
        dp[fuel, u, target] = ans
        return ans
