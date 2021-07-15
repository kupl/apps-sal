class Solution:
     def maximalSquare(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         if not matrix:
             return 0
 
         m, n = len(matrix), len(matrix[0])
         dp = [int(matrix[i][0]) for i in range(m)]
         vmax = max(dp)    
         pre = 0   
         for j in range(1, n):
             pre, dp[0] = int(matrix[0][j-1]), int(matrix[0][j])
             for i in range(1, m):
                 cur = dp[i]
                 dp[i] = 0 if matrix[i][j] == '0' else (min(dp[i-1], dp[i], pre) + 1) 
                 pre = cur
             vmax = max(vmax, max(dp))
         return vmax ** 2
