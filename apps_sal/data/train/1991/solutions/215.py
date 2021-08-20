class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        def dfs(cur, dp, f):
            if f < 0:
                return 0
            if dp[cur][f] != -1:
                return dp[cur][f]
            route = 0
            if cur == finish:
                route = 1
            for j in range(len(locations)):
                if cur != j:
                    route = (route + dfs(j, dp, f - abs(locations[cur] - locations[j]))) % mod
            dp[cur][f] = route
            return route
        dp = [[-1 for _ in range(fuel + 1)] for _ in range(len(locations))]
        return dfs(start, dp, fuel)
