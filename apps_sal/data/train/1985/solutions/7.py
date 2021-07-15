class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         if len(matrix)==0:
             return False
         minrow, maxcol = 0, len(matrix[0])-1
         
         while(minrow<len(matrix) and maxcol>=0):
             if target == matrix[minrow][maxcol]:
                 return True
             elif target < matrix[minrow][maxcol]:
                 maxcol-=1
             else:
                 minrow+=1
         return False
