class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (n, mod) = (len(locations), 1000000007)
        dp = [[0] * n for _ in range(fuel + 1)]
        for f in range(fuel + 1):
            for i in range(n):
                for j in range(n):
                    if j != i and f >= abs(locations[i] - locations[j]):
                        dp[f][i] += dp[f - abs(locations[i] - locations[j])][j]
            dp[f][finish] += 1
        return dp[fuel][start] % mod
