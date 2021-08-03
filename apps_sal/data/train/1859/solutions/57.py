class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
        summ = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                summ += dp[i][j]
        return summ
