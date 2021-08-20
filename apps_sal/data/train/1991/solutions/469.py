class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        n = len(locations)
        dp = [[0] * n for _ in range(201)]
        for f in range(201):
            dp[f][finish] = 1
        for ff in range(1, fuel + 1):
            for node in range(n):
                res = 0
                for (i, j) in enumerate(locations):
                    if i == node:
                        continue
                    need = abs(j - locations[node])
                    if need <= ff:
                        res = (res + dp[ff - need][i]) % mod
                dp[ff][node] = (res + dp[ff][node]) % mod
        return dp[fuel][start]
