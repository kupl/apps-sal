class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        cnt = 0
        (rows, cols) = (len(matrix), len(matrix[0]))
        dp = [[0] * (cols + 1) for i in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    cnt += dp[i][j]
        return cnt
