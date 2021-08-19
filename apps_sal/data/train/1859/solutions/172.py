class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        ret = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        ret += 1
                    else:
                        min_side = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                        matrix[i][j] = min_side
                        ret += min_side
        return ret
