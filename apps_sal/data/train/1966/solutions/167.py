# O(mn*mn) time and O(1) space
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len( mat )
        cols = len( mat[0] )

        \"\"\"
        For each row, determine the number of submatrices of all 1's
        that exist in that row. While moving horizontally along the
        row, count the submatrices that terminate at each location.
        Save the count of submatrices in the variable submatrices.
        \"\"\"
        submatrices = 0
        for r in range( rows ):
            submatrices += mat[r][0]
            for c in range( 1, cols ):
                if mat[r][c]:
                    if c > 0:
                        mat[r][c] = mat[r][c - 1] + 1
                    submatrices += mat[r][c]

        \"\"\"
        At this point we have counted the submatrices that exist
        within a single row. The code below counts the submatrices
        that span multiple rows, then returns the sum of the two
        counts.
        
        Process the above matrix one row at a time. Moving down each
        column, determine the number of submatrices of all 1's that
        start on that row looking left and span multiple rows.  Repeat
        for each row and return the total number of submatrices.

        For each 1 within a row, count the submatrices that contain
        the 1, start on the same row either at or before the 1, and
        span multiple rows. Proceed down the column that contains the 1
        until reaching a 0 or the bottom row of the matrix. While
        proceeding down a column, the width of the submatrices may
        stay the same or gets thinner.
        \"\"\"
        for r in range( rows - 1 ):
            for c in range( cols ):
                if mat[r][c]:
                    row = r + 1
                    submatrix_width = mat[r][c]
                    while row < rows and mat[row][c]:
                        submatrix_width = min( submatrix_width, mat[row][c] )
                        submatrices += submatrix_width
                        row += 1
        return submatrices
