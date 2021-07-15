class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        \"\"\"
        Assume:
        
        Algorithm:
        
        prefixsum
        1. row: from left to right
        2. col: from top to bottom
        
        xxxxxx
        xxxxxx
        xXXXXx
        xXXXXx
        xxxxxx
        
        result[i][j] = mat[i+K][j+K] - mat[i-K][j+K] - mat[i+K][j-K] + mat[i-K][j-K]
                            rmax cmax       rmin                 cmin
        need to consider boundary conditions
        
        \"\"\"
        
        m, n = len(mat), len(mat[0])
        range_sum = [[0]*(n+1) for _ in range(m+1)]
        result = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                range_sum[i+1][j+1] = range_sum[i][j+1] + range_sum[i+1][j] - range_sum[i][j] + mat[i][j]
        print(range_sum)
        for i in range(m):
            for j in range(n):
                rmin, rmax = max(0, i - K), min(m, i + K + 1)
                cmin, cmax = max(0, j - K), min(n, j + K + 1)
                result[i][j] = range_sum[rmax][cmax] - range_sum[rmin][cmax] - range_sum[rmax][cmin] + range_sum[rmin][cmin]
        return result
        
                
