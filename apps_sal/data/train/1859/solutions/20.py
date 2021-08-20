class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        totalRows = len(matrix)
        totalColumns = len(matrix[0])
        longestStreak = [[(0, 0, 0) for i in range(totalColumns)] for j in range(totalRows)]
        total = 0
        for i in range(totalRows):
            for j in range(totalColumns):
                if i == 0 and j == 0:
                    longestStreak[i][j] = (matrix[i][j], matrix[i][j], matrix[i][j])
                    total += matrix[i][j]
                elif i == 0:
                    longestStreak[i][j] = (matrix[i][j] * (longestStreak[i][j - 1][0] + 1), matrix[i][j], matrix[i][j])
                    total += matrix[i][j]
                elif j == 0:
                    longestStreak[i][j] = (matrix[i][j], matrix[i][j] * (longestStreak[i - 1][j][1] + 1), matrix[i][j])
                    total += matrix[i][j]
                else:
                    a = matrix[i][j] * (longestStreak[i][j - 1][0] + 1)
                    b = matrix[i][j] * (longestStreak[i - 1][j][1] + 1)
                    c = matrix[i][j] * (longestStreak[i - 1][j - 1][2] + 1)
                    longestStreak[i][j] = (a, b, min([a, b, c]))
                    total += min([a, b, c])
        return total
