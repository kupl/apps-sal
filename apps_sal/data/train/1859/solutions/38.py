class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if (rows == 0):
            return 0

        cols = len(matrix[0])
        if (cols == 0):
            return 0

        self.res = 0

        for r in range(rows):
            for c in range(cols):
                if (matrix[r][c] == 1):
                    if (r == 0 or c == 0):
                        self.res += 1
                    else:
                        cell_val = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + 1
                        self.res += cell_val
                        matrix[r][c] = cell_val

        return self.res
