class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        total_sub_matrix = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    max_col = len(mat[0])
                    for sub_row in range(row, len(mat)):
                        for sub_col in range(col, max_col):
                            if mat[sub_row][sub_col] == 0:
                                max_col = sub_col
                                break
                            total_sub_matrix += 1
        return total_sub_matrix
