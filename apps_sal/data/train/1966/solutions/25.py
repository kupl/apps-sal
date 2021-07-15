class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        # row_matrices[i][j] = num of submatrices in row i that ends in col j
        row_matrices = [[0] * cols for _ in range(rows)]
        
        # Count submatrices for every single row
        for i in range(rows):
            row_matrices[i][0] = mat[i][0]
            for j in range(1, cols):
                if mat[i][j] == 1:
                    row_matrices[i][j] = row_matrices[i][j - 1] + 1
                else:
                    row_matrices[i][j] = 0
        
        result = 0
        
        for i in range(rows):
            for j in range(cols):
                cur_min = float('inf')
                # Search upwards row by row
                for k in range(i, -1, -1):
                    if mat[k][j] == 0:
                        break
                        
                    # why min():
                    #   0, 1, 1, 1  r0
                    #   0, 0, 1, 1  r1
                    #   0, 1, 1, 1  r2
                    # the num of matrices will be bottlenecked by the row
                    # with minimum matrices. In this case, r1.
                    cur_min = min(cur_min, row_matrices[k][j])
                    result += cur_min
                    
        return result

