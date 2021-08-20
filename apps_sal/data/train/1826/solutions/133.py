class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        sum_mtx = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]
        for row in range(len(mat)):
            summ = 0
            for col in range(len(mat[0])):
                summ += mat[row][col]
                sum_mtx[row][col] = summ
                if row > 0:
                    sum_mtx[row][col] += sum_mtx[row - 1][col]
        output_img = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                max_row = min(len(mat) - 1, K + row)
                min_row = max(0, row - K)
                min_col = max(col - K, 0)
                max_col = min(col + K, len(mat[0]) - 1)
                (a_val, b_val, c_val) = (0, 0, 0)
                d_val = sum_mtx[max_row][max_col]
                if min_col > 0:
                    c_val = sum_mtx[max_row][min_col - 1]
                if min_row > 0:
                    b_val = sum_mtx[min_row - 1][max_col]
                if c_val and b_val:
                    a_val = sum_mtx[min_row - 1][min_col - 1]
                output_img[row][col] = d_val - b_val - c_val + a_val
        return output_img
