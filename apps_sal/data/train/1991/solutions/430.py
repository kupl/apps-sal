class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        (n, m) = (len(locations), fuel + 1)
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]
        for fuell in range(m):
            for current in range(n):
                ans = 0
                if current == finish:
                    ans += 1
                for j in range(n):
                    if j == current:
                        continue
                    cost = abs(locations[j] - locations[current])
                    if cost <= fuell:
                        ans += dp[fuell - cost][j]
                dp[fuell][current] = ans % MOD
        return dp[fuel][start]
