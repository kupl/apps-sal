import copy


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        matrix2 = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            start = matrix[i][0]
            for j in range(1, len(matrix[0])):
                start += matrix[i][j]
                matrix2[i][j] = start
        for j in range(len(matrix[0])):
            start = matrix2[0][j]
            for i in range(1, len(matrix)):
                start += matrix2[i][j]
                matrix2[i][j] = start
        res = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 1):
                    possible = min(row - i, col - j)
                    for t in range(possible):
                        length = t + 1
                        sums = matrix2[i + t][j + t]
                        if i - 1 >= 0:
                            sums -= matrix2[i - 1][j + t]
                        if j - 1 >= 0:
                            sums -= matrix2[i + t][j - 1]
                        if j - 1 >= 0 and i - 1 >= 0:
                            sums += matrix2[i - 1][j - 1]
                        if sums == length * length:
                            res += 1
                        else:
                            break
        return res
