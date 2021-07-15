class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         index_x = 0
         index_y = 0
         m = len(matrix)
         if m == 0:
             return False
         n = len(matrix[0])
         if n == 0:
             return False
         for num in range(n):
             if target == matrix[0][num]:
                 return True
             if target < matrix[0][num]:
                 index_x = num
                 break
             index_x = n
             
         for num in range(m):
             if target == matrix[num][0]:
                 return True
             if target < matrix[num][0]:
                 index_y = num
                 break
             index_y = m
             
         for x in range(index_x):
             for y in range(index_y):
                 if matrix[y][x] == target:
                     return True
         
         return False
