class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        matrix_sum = [ [0]*(n+1) for _ in range(m+1) ]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                matrix_sum[i][j] = matrix_sum[i][j-1] + matrix[i-1][j-1]
        
        for j in range(1, n+1):
            for i in range(1, m+1):
                matrix_sum[i][j] = matrix_sum[i][j] + matrix_sum[i-1][j]
        
        cnt = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                size = 1
                while size <= min(i,j):
                    total = matrix_sum[i][j] + matrix_sum[i-size][j-size] - matrix_sum[i-size][j]\\
                    - matrix_sum[i][j-size]
                    if total == size*size:
                        cnt += 1
                    else:
                        break
                    size += 1
        
        return cnt
        
        
