import numpy as np


class Solution:
    def matrixBlockSum(self, A, K):
        A = np.array(A)
        m, n = A.shape
        return [[A[max(i - K, 0):i + K + 1, max(j - K, 0):j + K + 1].sum()
                 for j in range(n)] for i in range(m)]
