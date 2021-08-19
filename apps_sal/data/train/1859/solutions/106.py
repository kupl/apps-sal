class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 1:
                    ul = matrix[row - 1][col - 1]
                    u = matrix[row - 1][col]
                    l = matrix[row][col - 1]
                    val = min(ul, u, l) + 1
                    matrix[row][col] = val
        total = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                total += matrix[row][col]
        return total
