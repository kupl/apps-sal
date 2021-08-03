class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        res, md = 0, 10**9 + 7
        n = len(locations)
        dp = [[0] * n for _ in range(fuel + 1)]
        dp[fuel][start] = 1
        for f in range(fuel, 0, -1):
            for i in range(n):
                for j in range(n):
                    if i != j:
                        need = abs(locations[i] - locations[j])
                        if f >= need:
                            dp[f - need][j] = (dp[f - need][j] + dp[f][i]) % md
        for f in range(fuel + 1):
            res = (res + dp[f][finish]) % md
        return res
