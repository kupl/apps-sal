class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[1])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                        res += matrix[i][j]
        return res
