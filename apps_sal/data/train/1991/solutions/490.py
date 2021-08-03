class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        n = len(locations)
        mod = int(1e9 + 7)
        dp = [[0 for i in range(n)] for j in range(fuel + 1)]

        dp[fuel][start] = 1

        for i in range(fuel, -1, -1):
            for x in range(n):
                for y in range(n):
                    if x == y:
                        continue
                    gas = abs(locations[x] - locations[y])
                    if i + gas <= fuel:
                        dp[i][x] = (dp[i][x] + dp[i + gas][y]) % mod

        res = 0
        for i in range(fuel + 1):
            res = (res + dp[i][finish]) % mod
        return res
