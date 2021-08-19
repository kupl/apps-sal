import numpy as np


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        arr = np.array([[0] * m] * n)
        mat = np.array(mat)
        for i in range(n):
            for j in range(m):
                cur = mat[i, j]
                if j - K < 0:
                    hor_s = slice(0, j + K + 1)
                else:
                    hor_s = slice(j - K, j + K + 1)
                if i - K < 0:
                    ver_s = slice(0, i + K + 1)
                else:
                    ver_s = slice(i - K, i + K + 1)
                arr[i, j] = mat[ver_s, hor_s].sum()
        return arr.tolist()
