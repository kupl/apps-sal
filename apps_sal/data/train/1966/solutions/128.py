class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        res = 0
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if mat[i - 1][j - 1]:
                    dp[i][j] = dp[i][j - 1] + 1
                    res += dp[i][j]
                    min_ones = dp[i][j]
                    for k in range(i - 1, -1, -1):
                        min_ones = min(min_ones, dp[k][j])
                        res += min_ones
        return res
