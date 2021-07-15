class Solution:
     def isToeplitzMatrix(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: bool
         """
         rows = len(matrix)
         col = len(matrix[0])
 
         i = 0
         j = 0
 
         while i < rows-1:
             while j < col-1:
                 print('Comparing: ',matrix[i][j], matrix[i + 1][j + 1])
                 if matrix[i][j] == matrix[i + 1][j + 1]:
                     j += 1
                 else:
                     return False
             i += 1
             j = 0
         return True
