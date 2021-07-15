class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])        
        mat[:] = [[0] * (n + 1)] + [[0] + row for row in mat]
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        # cum sum 
        for i in range(1, m+1):
            for j in range(1, n+1):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        
        # compute sums
        for i in range(m):
            for j in range(n):
                r1, c1 = max(i-K, 0), max(j-K, 0)
                r2, c2 = min(i+K+1, m), min(j+K+1, n)
                res[i][j] = mat[r2][c2] - mat[r1][c2] - mat[r2][c1] + mat[r1][c1]
        
        return res
                    
                    
        
                        

