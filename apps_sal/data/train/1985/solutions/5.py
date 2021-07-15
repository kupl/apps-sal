class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         if not matrix:
             return False
         m, n = len(matrix), len(matrix[0])
         row, col = m-1, 0
         while row >= 0 and col < n:
             if matrix[row][col] == target:
                 return True
             elif matrix[row][col] < target:
                 col += 1
             else:
                 row -= 1
         return False
