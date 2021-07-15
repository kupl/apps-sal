class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    continue
                if matrix[i][j-1] and matrix[i-1][j] and matrix[i-1][j-1]:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
        
        total = 0
        for row in matrix:
            total += sum(row)
            
        return total
                

