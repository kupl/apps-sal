class Solution:
    def matrixBlockSum(self, mat, K):
        # ok
        n = len(mat) ; m = len(mat[0])
        arr = [[0]*(m) for i in range(n)]
        for i in range( n ):
            for j in range(1, m):
                mat[i][j]+=mat[i][j-1]
        for j in range(m):
            for i in range(1,n):
                mat[i][j]+=mat[i-1][j]
        # [print(mat[i]) for i in range(n)]
        for i in range(n):
            for j in range(m):
                min_row, max_row = max( 0, i-K), min( n-1, i+K)
                min_col, max_col = max( 0, j-K), min( m-1, j+K)

                arr[i][j] = mat[max_row][max_col]

                if min_row > 0:
                    arr[i][j] -= mat[min_row-1][max_col]

                if min_col > 0:
                    arr[i][j] -= mat[max_row][min_col-1]

                if min_col > 0 and min_row > 0:
                    arr[i][j] += mat[min_row-1][min_col-1]
        return arr
