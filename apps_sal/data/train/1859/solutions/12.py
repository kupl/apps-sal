class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (m, n) = (len(matrix), len(matrix[0]))
        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    continue
                if r == 0 or c == 0:
                    res += 1
                else:
                    cell_val = min(matrix[r - 1][c - 1], matrix[r][c - 1], matrix[r - 1][c]) + matrix[r][c]
                    res += cell_val
                    matrix[r][c] = cell_val
        return res
