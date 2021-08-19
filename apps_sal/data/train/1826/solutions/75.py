import numpy as np


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        pre = [[0] * n for j in range(m)]
        for i in range(m):
            pre[i][0] = mat[i][0]
            for j in range(1, n):
                pre[i][j] = pre[i][j - 1] + mat[i][j]
        for i in range(n):
            pre[0][i] = pre[0][i]
            for j in range(1, m):
                pre[j][i] = pre[j - 1][i] + pre[j][i]
        for i in range(m):
            ru = max(i - k, 0)
            rd = min(i + k, m - 1)
            for j in range(n):
                cl = max(0, j - k)
                cr = min(n - 1, j + k)
                value = pre[rd][cr]
                if ru - 1 >= 0:
                    value -= pre[ru - 1][cr]
                if cl - 1 >= 0:
                    value -= pre[rd][cl - 1]
                if ru - 1 >= 0 and cl - 1 >= 0:
                    value += pre[ru - 1][cl - 1]
                mat[i][j] = value
        return mat
