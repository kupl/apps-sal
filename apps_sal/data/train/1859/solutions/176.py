class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        sm = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - 1 >= 0 and j - 1 >= 0 and (matrix[i][j] > 0) and (matrix[i][j - 1] > 0) and (matrix[i - 1][j] > 0) and (matrix[i - 1][j - 1] > 0):
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                sm += matrix[i][j]
        return sm
