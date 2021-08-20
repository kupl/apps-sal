class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (m, n) = (len(matrix), len(matrix[0]))
        dp = [[0] * n for _ in range(m)]
        squares = 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    continue
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                squares += dp[i][j]
        return squares
