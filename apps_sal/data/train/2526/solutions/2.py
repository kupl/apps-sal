class Solution:
     def trailingZeroes(self, n):
         """
         :type n: int
         :rtype: int
         """
         count = 1
         a = 5
         ans = 0
         
         while a<=n:
             ans += n//a
             count += 1
             a = 5**count
             
         return ans

