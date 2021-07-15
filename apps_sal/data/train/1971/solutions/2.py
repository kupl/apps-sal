class Solution:
     def maximalSquare(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         if not matrix: return 0
         rows, cols = len(matrix), len(matrix[0])
         dp = list(map(int, matrix[0][:]))
         maxLen = 1 if sum(dp) > 0 else 0
         for i in range(1, rows):
             tmp = dp[0]
             dp[0] = int(matrix[i][0])
             maxLen = max(maxLen, dp[0])
             pre = tmp
             for j in range(1, cols):
                 tmp = dp[j]
                 if matrix[i][j] == '1':
                     dp[j] = min(dp[j], dp[j - 1], pre) + 1
                     maxLen = max(maxLen, dp[j])
                 else:
                      dp[j] = 0
                 pre = tmp
         return maxLen * maxLen
