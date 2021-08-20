class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[-1 for _ in range(fuel)] for _ in range(n)]
        r = self.helper(locations, start, dp, fuel, finish)
        print(dp)
        return r

    def helper(self, locations, cur, dp, fuel, ed):
        if fuel < 0:
            return 0
        if dp[cur][fuel - 1] != -1:
            return dp[cur][fuel - 1]
        n = len(locations)
        r = 0
        if cur == ed:
            r += 1
        for i in range(n):
            if i != cur:
                r += self.helper(locations, i, dp, fuel - abs(locations[cur] - locations[i]), ed)
        dp[cur][fuel - 1] = r % (10 ** 9 + 7)
        return dp[cur][fuel - 1]
