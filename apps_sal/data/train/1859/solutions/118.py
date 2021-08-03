class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        max_y = len(matrix)
        max_x = len(matrix[0])

        for y in range(1, max_y):
            for x in range(1, max_x):
                if matrix[y][x] and matrix[y][x - 1] and matrix[y - 1][x] and matrix[y - 1][x - 1]:
                    matrix[y][x] = min(matrix[y][x - 1], matrix[y - 1][x], matrix[y - 1][x - 1]) + 1

        row_sums = [sum(row) for row in matrix]
        return sum(row_sums)
