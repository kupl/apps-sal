import numpy as np


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mat = np.array(mat)
        answer = np.zeros(mat.shape)
        for i, row in enumerate(mat):
            row_start = max([0, i - K])
            row_end = min([mat.shape[0], i + K])
            for j, col in enumerate(row):
                col_start = max([0, j - K])
                col_end = min([mat.shape[1], j + K])
                # TODO:
                answer[i][j] = np.sum(mat[row_start:row_end + 1, col_start:col_end + 1])
        return answer.astype(np.int)
