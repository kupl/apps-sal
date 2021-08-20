class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (m, n) = (len(matrix), len(matrix[0]))
        ans = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    matrix[i][j] *= min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                ans += matrix[i][j]
        return ans
