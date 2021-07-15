class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        

        rows = len( mat )
        cols = len( mat[0] )


        for r in range( rows ):
            for c in range( 1, cols ):
                if mat[r][c]:
                    if c > 0:
                        mat[r][c] = mat[r][c - 1] + 1

        
        submatrices = 0
        for r in range( rows ):
            for c in range( cols ):
                if mat[r][c]:
                    row = r
                    submatrix_width = mat[r][c]
                    while row < rows and mat[row][c]:
                        submatrix_width = min( submatrix_width, mat[row][c] )
                        submatrices += submatrix_width
                        row += 1
        return submatrices

