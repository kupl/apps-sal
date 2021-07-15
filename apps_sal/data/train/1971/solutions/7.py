class Solution:
     def maximalSquare(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         if len(matrix) == 0 or len(matrix[0]) == 0:
             return 0
         
         dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
         
         largest = 0;
         for i in range(len(matrix)):
             dp[i][0] = int(matrix[i][0])
             largest = max(largest, dp[i][0])
             
         for j in range(len(matrix[0])):
             dp[0][j] = int(matrix[0][j])
             largest = max(largest , dp[0][j])
             
         
         
         for i in range(1, len(matrix)):
             for j in range(1, len(matrix[0])):
                 if matrix[i][j] == '1':
                     if dp[i - 1][j] >= dp[i - 1][j - 1] and dp[i][j - 1] >= dp[i - 1][j - 1]:
                         dp[i][j] = dp[i - 1][j - 1] + 1
 
                     else:
                         dp[i][j] = min(int(dp[i - 1][j]), int(dp[i][j - 1])) + 1
                 else:
                     dp[i][j] = 0
                 
                 largest = max(largest, dp[i][j])
         
         
         return largest * largest

