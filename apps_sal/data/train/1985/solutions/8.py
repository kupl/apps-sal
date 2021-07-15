class Solution:
     def searchMatrix(self, matrix, k):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         for i in range(len(matrix)):
             for j in range(len(matrix[i])):
                 if k < matrix[i][j] or k > matrix[i][len(matrix[i])-1]:
                     break
                 elif matrix[i][j] == k:
                     return True
         return False
                 
          

