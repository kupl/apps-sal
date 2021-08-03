class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        temp = min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j]) + 1
                        res += temp
                        matrix[i][j] = temp

        return res
