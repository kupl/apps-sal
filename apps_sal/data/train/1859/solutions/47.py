class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:

        def get(i, j):
            if i < 0 or j < 0:
                return 0
            elif i > len(matrix) or j > len(matrix[0]):
                return 0
            return matrix[i][j]
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 1:
                    continue
                squares = min(get(i - 1, j - 1), get(i - 1, j), get(i, j - 1)) + 1
                matrix[i][j] = squares
                count += squares
        return count
