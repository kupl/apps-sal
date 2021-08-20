class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        distances = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                distances[i][j] = abs(locations[i] - locations[j])
                distances[j][i] = distances[i][j]
        mod = 1000000007
        dp = [[0] * n for i in range(fuel + 1)]
        dp[0][finish] = 1
        for f in range(1, fuel + 1):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    else:
                        dist = distances[i][j]
                        if f - dist >= 0:
                            dp[f][i] += dp[f - dist][j]
        res = 0
        for i in range(fuel + 1):
            res += dp[i][start]
        return res % mod
