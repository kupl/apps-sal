class Solution:
     def isToeplitzMatrix(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: bool
         """
         
         x, y = len(matrix[0]), len(matrix)
         
         for i in range(x - 1):
             for j in range(y - 1):
                 if matrix[j][i] != matrix[j+1][i+1]:
                     return False
         return True
         """
         starters = [[0, i] for i in range(x)] + [[i, 0] for i in range(y)]
         for starter in starters:
             for j in range(min(x,y)):
                 if starter[0] + j < y and starter[1] + j < x:
                     print(starter[0] + j , starter[1] + j)
                     if matrix[starter[0]][starter[1]] != matrix[starter[0] + j][starter[1] + j]:
                         return False
             print('\n')
         return True
         """
