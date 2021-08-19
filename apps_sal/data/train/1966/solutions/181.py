class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        #         rows = len( mat )
        #         cols = len( mat[0] )

        #         for r in range( rows ):
        #             for c in range( 1, cols ):
        #                 if mat[r][c]:
        #                     if c > 0:
        #                         mat[r][c] = mat[r][c - 1] + 1

        #         submatrices = 0
        #         for r in range( rows ):
        #             for c in range( cols ):
        #                 if mat[r][c]:
        #                     row = r
        #                     submatrix_width = mat[r][c]
        #                     while row < rows and mat[row][c]:
        #                         submatrix_width = min( submatrix_width, mat[row][c] )
        #                         submatrices += submatrix_width
        #                         row += 1
        #         return submatrices

        res = 0

        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j]:
                    if j > 0:
                        mat[i][j] = mat[i][j - 1] + 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    r = i
                    wid = mat[i][j]
                    while r < len(mat) and mat[r][j]:
                        wid = min(mat[r][j], wid)
                        res += wid
                        r += 1
        return res
