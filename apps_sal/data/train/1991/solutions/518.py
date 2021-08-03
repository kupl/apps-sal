class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0 for i in range(fuel + 1)] for i in range(n)]
        mod = 10 ** 9 + 7

        dp[start][fuel] = 1
        for k in range(fuel, -1, -1):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    diff = abs(locations[i] - locations[j])

                    if diff <= k:
                        dp[j][k - diff] = (dp[j][k - diff] + dp[i][k]) % mod

        ans = 0
        for i in dp[finish]:
            ans = (ans + i) % mod
        return ans
