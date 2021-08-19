class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] and r > 0 and (c > 0):
                    matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]) + 1
                count += matrix[r][c]
        return count
