class Solution:
     def isToeplitzMatrix(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: bool
         """
         if not matrix:
             return False
         colSize = len(matrix[0]) - 1
         for row in range(len(matrix) - 1):
             if matrix[row][:colSize] != matrix[row+1][1:colSize+1]:
                 return False
         return True
