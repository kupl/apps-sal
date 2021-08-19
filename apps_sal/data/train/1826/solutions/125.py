class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        k = K
        (n, m) = (len(mat), len(mat[0]))
        matrix = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            matrix.append(temp)
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    summ = 0
                    for o in range(min(n, k + 1)):
                        for l in range(min(m, k + 1)):
                            summ += mat[o][l]
                    matrix[i][j] = summ
                elif j == 0:
                    summ = 0
                    remSumm = 0
                    for l in range(min(m, k + 1)):
                        if i + k <= n - 1:
                            summ += mat[i + k][l]
                        if i - k - 1 >= 0:
                            remSumm += mat[i - k - 1][l]
                    print((i, j, matrix[i - 1][j], summ, remSumm))
                    matrix[i][j] = matrix[i - 1][j] + summ - remSumm
                else:
                    summ = 0
                    remSumm = 0
                    for l in range(max(0, i - k), min(n, i + k + 1)):
                        if j + k <= m - 1:
                            summ += mat[l][j + k]
                        if j - k - 1 >= 0:
                            remSumm += mat[l][j - k - 1]
                    print((i, j, matrix[i][j - 1], summ, remSumm))
                    matrix[i][j] = matrix[i][j - 1] + summ - remSumm
        return matrix
