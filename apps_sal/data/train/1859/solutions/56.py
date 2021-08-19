from itertools import chain as chain


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                else:
                    matrix[i][j] = 0
        return sum(chain(*matrix))
