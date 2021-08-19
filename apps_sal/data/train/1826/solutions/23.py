import numpy as np


class Solution:

    def matrixBlockSum(self, mat, k):
        p = 2 * k + 1
        (m, n) = (len(mat), len(mat[0]))
        array = np.zeros((m + p, n + p), dtype=np.uint32)
        array[k + 1:-k, k + 1:-k] = mat
        np.cumsum(array, axis=0, out=array)
        np.cumsum(array, axis=1, out=array)
        return array[p:, p:] - array[p:, :-p] - array[:-p, p:] + array[:-p, :-p]
