class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1] * (fuel + 1) for _ in range(n)]

        def dfs(locations, p, finish, f, dp):
            if f < 0:
                return 0
            if dp[p][f] != -1:
                return dp[p][f]
            res = 0
            if p == finish:
                res += 1
            for i in range(n):
                if i != p:
                    res += dfs(locations, i, finish, f - abs(locations[i] - locations[p]), dp) % (10 ** 9 + 7)
            dp[p][f] = res
            return res % (10 ** 9 + 7)
        return dfs(locations, start, finish, fuel, dp)
