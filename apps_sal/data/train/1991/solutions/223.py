class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for _ in range(len(locations))] for _ in range(fuel + 1)]
        dp[fuel][start] = 1
        for f in range(fuel, -1, -1):
            for (i, c) in enumerate(dp[f]):
                if c > 0:
                    for (j, loc) in enumerate(locations):
                        if i != j and abs(locations[i] - loc) <= f:
                            dp[f - abs(locations[i] - loc)][j] += c
        return sum([dp[i][finish] for i in range(fuel + 1)]) % (10 ** 9 + 7)
