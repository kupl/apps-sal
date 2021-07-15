class Solution:
     def maximalSquare(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         m, n = len(matrix), len(matrix[0]) if matrix else 0
         dp = [0]*n
         best = 0
         for r in range(m):
             ndp = [0]*n
             for c in range(n):
                 if matrix[r][c] == '1':
                     ndp[c] = min(dp[c-1], dp[c], ndp[c-1])+1 if r and c else 1
                     if ndp[c] > best:
                         best = ndp[c]
             dp = ndp
         return best**2
