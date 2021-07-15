class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        submatrices = 0
        for r in range(rows):
            submatrices += mat[r][0]
            for c in range(1,cols):
                if mat[r][c] != 0:
                    if c > 0:
                        mat[r][c] = mat[r][c - 1] + 1
                    submatrices += mat[r][c]
            
                    
               
        for r in range(rows - 1):
            for c in range(cols):
                if mat[r][c] != 0:
                    row = r + 1
                    submatrix_width = mat[r][c]
                    while row < rows and mat[row][c] != 0:
                        submatrix_width = min(submatrix_width,mat[row][c])
                        
                        submatrices += submatrix_width
                        row += 1
        return submatrices
