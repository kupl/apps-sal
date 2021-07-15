class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        diag = 0
        square = [matrix[i][:] for i in range(m)]
        total = 0
        r, c = 0, 0
        while diag < m+n-1:
            if 0<r<m and 0<c<n and matrix[r][c]>0:
                square[r][c] += min(square[r][c-1], square[r-1][c], square[r-1][c-1])
            total += square[r][c]  
            r += 1
            c -= 1
            if (r>m-1) or (c<0):
                diag += 1
                r = 0 if diag<n else diag-n+1
                c = diag - r
        return total
                
                
                
                

