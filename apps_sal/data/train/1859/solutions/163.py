class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n, count = len(matrix), len(matrix[0]), 0
        size_matrix = [[0] * n for j in range(m)]
        indices = [(-1, -1), (-1, 0), (0, -1)]

        def _in_range(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        size_matrix[i][j] = matrix[i][j]
                        if matrix[i][j] == 1:
                            count += 1
                    else:
                        minimum = min([size_matrix[x + i][y + j] for x, y in indices if _in_range(x + i, y + j)])
                        size_matrix[i][j] = minimum + 1
                        count += 1 + minimum

        return count
