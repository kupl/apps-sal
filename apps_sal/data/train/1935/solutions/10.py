class Solution:

    def isToeplitzMatrix(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                r = i + 1
                c = j + 1
                while r < len(matrix) and c < len(matrix[0]):
                    if matrix[i][j] == matrix[r][c]:
                        r += 1
                        c += 1
                        continue
                    else:
                        return False
        return True
