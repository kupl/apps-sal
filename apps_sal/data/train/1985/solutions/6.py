class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         if len(matrix) == 0 or len(matrix[0]) == 0:
             return False
         m = 0
         n = len(matrix[0]) - 1
         while m < len(matrix) and n >= 0:
             if target == matrix[m][n]:
                 return True
             elif target < matrix[m][n]:
                 n -= 1
             elif target > matrix[m][n]:
                 m += 1
         return False
