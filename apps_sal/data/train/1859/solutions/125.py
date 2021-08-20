def checkCorners(row_size, col_size, r, c):
    if (0 <= r - 1 < row_size and 0 <= c < col_size) and (0 <= r - 1 < row_size and 0 <= c - 1 < col_size) and (0 <= r < row_size and 0 <= c - 1 < col_size):
        return True
    return False


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix[:]
        r_size = len(matrix)
        c_size = len(matrix[0])
        acc = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1 and checkCorners(r_size, c_size, row, col):
                    dp[row][col] += min(matrix[row][col - 1], matrix[row - 1][col], matrix[row - 1][col - 1])
                acc += dp[row][col]
        return acc
