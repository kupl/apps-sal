class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0] * (fuel + 1) for _ in range(len(locations))]
        for i in range(fuel + 1):
            dp[finish][i] = 1
        for j in range(fuel + 1):
            for i in range(len(locations)):
                for k in range(len(locations)):
                    if i == k:
                        continue
                    cost = abs(locations[i] - locations[k])
                    if cost <= j:
                        dp[i][j] += dp[k][j - cost]

        return dp[start][fuel] % (10**9 + 7)
