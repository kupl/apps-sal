class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != 0 and matrix[i - 1][j] != 0 and (matrix[i][j - 1] != 0) and (matrix[i - 1][j - 1] != 0):
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        for i in matrix:
            ans += sum(i)
        return ans
