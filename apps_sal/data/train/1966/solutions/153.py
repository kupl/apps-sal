class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            dp[i][0] = 1 if mat[i][0] == 1 else 0
            res += dp[i][0]
            mini = dp[i][0]
            for k in range(i - 1, -1, -1):
                mini = min(mini, dp[k][0])
                res += mini
                if mini == 0:
                    break

            for j in range(1, n):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                    res += dp[i][j]

                    mini = dp[i][j]
                    for k in range(i - 1, -1, -1):
                        mini = min(mini, dp[k][j])
                        res += mini
                        if mini == 0:
                            break
        return res
