class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        for i in range(fuel + 1):
            dp[finish][i] = 1
        for i in range(1, fuel + 1):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    dist = abs(locations[j] - locations[k])
                    if dist <= i:
                        dp[j][i] += dp[k][i - dist] % (1000000000.0 + 7)
        return int(dp[start][fuel] % (1000000000.0 + 7))
