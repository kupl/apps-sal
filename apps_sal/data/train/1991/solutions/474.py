class Solution:
    def countRoutes(self, loc: List[int], s: int, t: int, F: int) -> int:
        N = len(loc)
        dp = [[0 for j in range(N)] for i in range(F + 1)]
        for i in range(F + 1):
            dp[i][t] = 1

        for f in range(1, F + 1):
            for i in range(len(loc)):
                for j in range(len(loc)):
                    if j != i:
                        d = f - abs(loc[i] - loc[j])
                        if d < 0:
                            continue
                        dp[f][i] += dp[d][j]
        return dp[F][s] % (10 ** 9 + 7)
