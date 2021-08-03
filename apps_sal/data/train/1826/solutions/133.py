
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        #i - K <= r <= i + K
        # [0][0]
        #0 - 1 <= r <= 1
        #   -1 <= r <= 1
        #j - K <= c <= j + K
        #   -1 <= c <= 1
        # => square with x=2
        #a[0][0] = row0+row1+col0+col1
        #        = 1+2=3+4+5 = 12

        #k = 1
        # [1][0]
        # 1-1=0 <= r <= 2
        # 1+2+4+5+7+8=?=27 yes

        sum_mtx = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]

        # new matrix that is sum of prev_sum + curr_val
        #[31, 2, 4]
        #[12, 26, 9]
        # =>
        # [31, 33, 37] #curr_sum = left_sum + curr_val
        # [43, 71 84] #1:43+ 2 + 26 = 71 =
        #                                   71  + 9 + 4 = 84
        # sum_mtx[0][0] = mat[0][0] #don't need
        for row in range(len(mat)):
            # reset each row
            summ = 0
            for col in range(len(mat[0])):
                # left_sum(without the its above_sum) + curr_val
                summ += mat[row][col]  # ONLY summing horizontals
                sum_mtx[row][col] = summ

                # for !row=0
                if row > 0:
                    #(left_sum* + curr_val + above_sum)
                    sum_mtx[row][col] += sum_mtx[row - 1][col]
        # above mtx allows us to just select the 4 idxes instead of having to repeatedly compute the sums of the blocks:a,b,c,d every time
        # print(sum_mtx)

        output_img = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                # the \"window\": like a zoom feature
                max_row = min(len(mat) - 1, K + row)
                min_row = max(0, row - K)
                min_col = max(col - K, 0)
                max_col = min(col + K, len(mat[0]) - 1)
                a_val, b_val, c_val = 0, 0, 0
                d_val = sum_mtx[max_row][max_col]

                if min_col > 0:
                    c_val = sum_mtx[max_row][min_col - 1]

                if min_row > 0:
                    b_val = sum_mtx[min_row - 1][max_col]

                if c_val and b_val:  # both exist
                    a_val = sum_mtx[min_row - 1][min_col - 1]

                output_img[row][col] = d_val - b_val - c_val + a_val
        return output_img
