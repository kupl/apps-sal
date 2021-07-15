class Solution:
     def isToeplitzMatrix(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: bool
         """
         return all(True if len(matrix[i])==1 or matrix[i][:-1]==matrix[i+1][1:] \
                    else False for i in range(len(matrix)-1))
