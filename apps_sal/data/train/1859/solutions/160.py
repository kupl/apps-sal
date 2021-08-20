class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        m = len(matrix)
        n = len(matrix[0])

        def invalid_matrix(r, c, s):
            for i in range(0, s):
                for j in range(s):
                    if r + i >= m or c + j >= n:
                        return True
                    if r + i < m and c + j < n and (matrix[r + i][c + j] == 0):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    count += 1
                    size = 2
                    while True:
                        if invalid_matrix(i, j, size):
                            break
                        count += 1
                        size += 1
        return count
