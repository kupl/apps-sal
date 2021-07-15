class Solution:
     def trailingZeroes(self, n):
         """
         :type n: int
         :rtype: int
         """
         count = 0
         while n > 0:
             n /= 5
             count += int(n)
         return int(count)
