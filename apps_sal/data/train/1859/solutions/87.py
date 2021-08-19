class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                re = 0
                if i > 0:
                    re += matrix[i - 1][j]
                if j > 0:
                    re += matrix[i][j - 1]
                if i > 0 and j > 0:
                    re -= matrix[i - 1][j - 1]
                matrix[i][j] += re
        print(matrix)
        re = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l = 0
                while i + l < len(matrix) and j + l < len(matrix[0]):
                    tmp = matrix[i + l][j + l]
                    if j > 0:
                        tmp -= matrix[i + l][j - 1]
                    if i > 0:
                        tmp -= matrix[i - 1][j + l]
                    if i > 0 and j > 0:
                        tmp += matrix[i - 1][j - 1]
                    if tmp != (l + 1) ** 2:
                        break
                    else:
                        re += 1
                    l += 1
        return re
