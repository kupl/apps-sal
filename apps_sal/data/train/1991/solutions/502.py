class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(len(locations) + 1)] for _ in range(fuel + 1)]
        dp[fuel][start] = 1
        for f in range(fuel, -1, -1):
            for i in range(len(locations)):
                for j in range(len(locations)):
                    if i == j:
                        continue
                    cost = abs(locations[j] - locations[i])
                    if cost + f <= fuel:
                        dp[f][i] += dp[f + cost][j]
        # print(dp)
        return sum([dp[f][finish] for f in range(fuel + 1)]) % MOD
