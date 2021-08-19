class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 for _ in locations] for _ in range(fuel + 1)]
        for f in range(1, fuel + 1):
            for (i, l) in enumerate(locations):
                dp[f][i] += sum([dp[f - abs(l - lj)][j] * int(i != j) for (j, lj) in enumerate(locations) if f >= abs(l - lj)])
                dp[f][i] += int(abs(l - locations[finish]) <= f and i != finish)
                dp[f][i] %= 10 ** 9 + 7
        for row in dp:
            print(row)
        return dp[fuel][start] if start != finish else dp[fuel][start] + 1 % (10 ** 9 + 7)
