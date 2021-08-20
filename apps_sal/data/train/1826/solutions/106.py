import numpy as np


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        size_row = len(mat)
        size_col = len(mat[0])
        in_mat = np.array(mat)
        res = np.zeros((size_row, size_col), dtype=np.int32)
        res_cell = 0
        r_min = 0
        r_max = min(size_row - 1, K)
        c_min = 0
        c_max = min(size_col - 1, K)
        for row in in_mat[0:r_max + 1, 0:c_max + 1]:
            res_cell += sum(row)
        remove_sum_right = 0
        add_sum_right = 0
        for i in range(size_row):
            if i != 0:
                r_min = max(0, i - K)
                r_max = min(size_row - 1, i + K)
                remove_sum_down = 0 if i - K <= 0 else np.sum(in_mat[r_min - 1:r_min, :min(K + 1, size_col)], axis=1)
                add_sum_down = 0 if i + K > size_row - 1 else np.sum(in_mat[r_max:r_max + 1, :min(K + 1, size_col)], axis=1)
                res_cell = res[i - 1][0] + add_sum_down - remove_sum_down
            for j in range(size_col):
                if j == 0:
                    res[i][j] = res_cell
                    continue
                c_min = max(0, j - K)
                c_max = min(size_col - 1, j + K)
                remove_sum_right = 0 if j - K <= 0 else np.sum(in_mat[r_min:r_max + 1, c_min - 1:c_min], axis=0)
                add_sum_right = 0 if j + K > size_col - 1 else np.sum(in_mat[r_min:r_max + 1, c_max:c_max + 1], axis=0)
                res[i][j] = res_cell + add_sum_right - remove_sum_right
                res_cell = res[i][j]
        return res
