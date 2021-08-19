class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        total = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                total += matrix[i][j]
        return total
