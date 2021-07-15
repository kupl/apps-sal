import numpy as np

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mat = np.array(mat)
        answer = np.zeros(mat.shape)
        for i, row in enumerate(mat):
            row_start = max([0, i - K])
            row_end = min([mat.shape[0] -1, i + K])
            # Each new row, reinitialize the value and add/remove newly in/out of range items
            if i > 0:
                col_start = 0
                col_end = min([mat.shape[1] -1, K])
                val = answer[i - 1][0]
                # Add the new row to the sum
                if i + K <= mat.shape[0] -1:
                    val += np.sum(mat[row_end,col_start:col_end + 1])
                # Remove out of range row
                if row_start > 0:
                    val -= np.sum(mat[row_start -1,col_start:col_end + 1])
            for j, col in enumerate(row):
                col_start = max([0, j - K])
                col_end = min([mat.shape[1] -1, j + K])
                print((row_start, row_end, col_start, col_end))
                if i == 0 and j == 0:
                    val = np.sum(mat[row_start:row_end + 1, col_start:col_end + 1])
                else:
                    # Add the new column to the sum
                    if j + K <= mat.shape[1] -1 and j != 0:
                        val += np.sum(mat[row_start:row_end + 1,col_end])
                    # Remove out of range column
                    if col_start > 0:
                        val -= np.sum(mat[row_start:row_end + 1,col_start - 1])
                answer[i][j] = val
        return answer.astype(np.int)
            
            

