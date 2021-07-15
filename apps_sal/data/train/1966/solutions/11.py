class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        nrows = len(mat)
        ncols = len(mat[0])
        
        for i in range(nrows):
            for j in range(ncols):
                if mat[i][j]:
                    if j > 0:
                        mat[i][j] = mat[i][j - 1] + 1
        
        cnt = 0
        
        for i in range(nrows):
            for j in range(ncols):
                if mat[i][j]:
                    row = i
                    submatrix_width = mat[i][j]
                    
                    while row < nrows and mat[row][j]:
                        submatrix_width = min(submatrix_width, mat[row][j])
                        cnt += submatrix_width
                        row += 1
        return cnt


                

