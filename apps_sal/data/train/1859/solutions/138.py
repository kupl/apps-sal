class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        memo = [[0] * m for i in range(n)]
        memo[0][0] = (matrix[0][0], matrix[0][0])
        for i in range(1, m):
            memo[0][i] = (memo[0][i - 1][0] + matrix[0][i], matrix[0][i])
        for i in range(1, n):
            memo[i][0] = (memo[i - 1][0][0] + matrix[i][0], matrix[i][0])
        for i in range(1, n):
            for j in range(1, m):
                # if matrix[i-1][j-1] == 0 or matrix[i][j] == 0:
                #     memo[i][j] = (memo[i-1][j][0] + memo[i][j-1][0] - memo[i-1][j-1][0] + matrix[i][j], matrix[i][j])
                # else:
                if matrix[i][j] == 0:
                    square_size = 0
                else:
                    square_size = min(memo[i - 1][j][1], memo[i][j - 1][1], memo[i - 1][j - 1][1])
                memo[i][j] = (memo[i - 1][j][0] + memo[i][j - 1][0] - memo[i - 1][j - 1][0] + (square_size + 1) * matrix[i][j], square_size + matrix[i][j])
        return memo[-1][-1][0]
