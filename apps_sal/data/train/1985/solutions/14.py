class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         height = len(matrix)
         if height == 0:
             return False
         width = len(matrix[0])
         def search(x, y):
             if x < 0 or y < 0 or x >= height or y >= width:
                 return False
             current = matrix[x][y]
             if current == target:
                 return True
             if current == None:
                 return False
             matrix[x][y] = None
             if current > target:
                 return search(x, y-1) or search(x-1, y)
             if current < target:
                 return search(x, y+1) or search(x+1, y)
         return search(0, 0)
         

