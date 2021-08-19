class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for x in range(n + 1)] for l in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] != 0:
                    dp[i][j] = matrix[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return sum([sum(x) for x in dp])
