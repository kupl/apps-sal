from collections import defaultdict
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            res += matrix[i][0]
        
        for j in range(1,len(matrix[0])):
            res += matrix[0][j]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
                res += matrix[i][j]
        print(matrix)
        return res
        
            

