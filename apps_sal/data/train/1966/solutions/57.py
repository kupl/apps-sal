class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        m, n = len(mat), len(mat[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1]:
                    dp[i][j] = dp[i][j - 1] + 1  # walk left
                    res += dp[i][j]
                    # walk above
                    min_ones = dp[i][j]
                    for k in range(i - 1, -1, -1):
                        min_ones = min(min_ones, dp[k][j])
                        res += min_ones
        return res
