class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        r = len(matrix)
        c = len(matrix[0])
        res = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        k = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + matrix[i][j]
                        res += k
                        matrix[i][j] = k
        return res
