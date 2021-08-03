class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    total += min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1

        return total
