class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        h, w = len(matrix), len(matrix[0])
        acc_mat, merge_status_mat = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]

        for i in range(h):
            for j in range(w):

                if j - 1 >= 0:
                    left = acc_mat[i][j - 1]
                    left_status = merge_status_mat[i][j - 1]
                else:
                    left = 0
                    left_status = 0

                if i - 1 >= 0:
                    top = acc_mat[i - 1][j]
                    top_status = merge_status_mat[i - 1][j]
                else:
                    top = 0
                    top_status = 0

                if i - 1 >= 0 and j - 1 >= 0:
                    topLeft = acc_mat[i - 1][j - 1]
                    topLeft_status = merge_status_mat[i - 1][j - 1]
                else:
                    topLeft = 0
                    topLeft_status = 0

                merge_status_mat[i][j] = min(topLeft_status, top_status, left_status) + 1 if matrix[i][j] == 1 else 0
                acc_mat[i][j] = left + top - topLeft + merge_status_mat[i][j]

        return acc_mat[i][j]
