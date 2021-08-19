class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat) + 1
        cols = len(mat[0]) + 1
        dp = [[0 for x in range(cols)] for y in range(rows)]
        for i in range(1, rows):
            dp[i][0] = 0
        for j in range(1, cols):
            dp[0][j] = 0

        res = 0
        # left most
        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i - 1][j - 1] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                    res += dp[i][j]
                    min_ones = dp[i][j]
                    # upper most
                    for k in range(i - 1, -1, -1):
                        min_ones = min(dp[k][j], min_ones)
                        res += min_ones
        return res
