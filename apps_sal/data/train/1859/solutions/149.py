
# 1277. Count Square Submatrices with All Ones

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        A = matrix
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
                
        # return sum(map(sum, A))
        return sum([A[i][j] for i in range(len(A)) for j in range(len(A[0]))])
    
# 1. class Solution:
# 2.     def countSquares(self, matrix: List[List[int]]) -> int:
# 3.         if matrix is None or len(matrix) == 0:
# 4.             return 0
# 5.         
# 6.         rows = len(matrix)
# 7.         cols = len(matrix[0])
# 8.         
# 9.         result = 0
# 10.         
# 11.         for r in range(rows):
# 12.             for c in range(cols):
# 13.                 if matrix[r][c] == 1:   
# 14.                     if r == 0 or c == 0: # Cases with first row or first col
# 15.                         result += 1      # The 1 cells are square on its own               
# 16.                     else:                # Other cells
# 17.                         cell_val = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
# 18.                         result += cell_val
# 19.                         matrix[r][c] = cell_val #**memoize the updated result**
# 20.         return result  

