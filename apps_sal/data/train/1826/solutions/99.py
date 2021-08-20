import numpy as np


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mat = np.array(mat)
        answer = np.zeros(mat.shape)
        for (i, row) in enumerate(mat):
            row_start = max([0, i - K])
            row_end = min([mat.shape[0] - 1, i + K])
            if i > 0:
                col_start = 0
                col_end = min([mat.shape[1] - 1, K])
                val = answer[i - 1][0]
                if i + K <= mat.shape[0] - 1:
                    val += np.sum(mat[row_end, col_start:col_end + 1])
                if row_start > 0:
                    val -= np.sum(mat[row_start - 1, col_start:col_end + 1])
            for (j, col) in enumerate(row):
                col_start = max([0, j - K])
                col_end = min([mat.shape[1] - 1, j + K])
                print((row_start, row_end, col_start, col_end))
                if i == 0 and j == 0:
                    val = np.sum(mat[row_start:row_end + 1, col_start:col_end + 1])
                else:
                    if j + K <= mat.shape[1] - 1 and j != 0:
                        val += np.sum(mat[row_start:row_end + 1, col_end])
                    if col_start > 0:
                        val -= np.sum(mat[row_start:row_end + 1, col_start - 1])
                answer[i][j] = val
        return answer.astype(np.int)
