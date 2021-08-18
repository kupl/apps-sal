import numpy as np


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        mat_np = np.array(mat)

        M, N = mat_np.shape

        sum_np = np.zeros((M, N), dtype=int)

        for m in range(M):

            for n in range(N):

                sum_np[m, n] = np.sum(mat_np[max(0, m - K):min(m + K + 1, M + 1),

                                             max(0, n - K):min(n + K + 1, N + 1)])

        return sum_np.tolist()
