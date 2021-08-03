class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        c = 0
        dp = matrix
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] != 0:
                    if dp[i - 1][j] != 0 and dp[i - 1][j - 1] != 0 and dp[i][j - 1] != 0:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

        for i in dp:
            c += sum(i)

        return c
