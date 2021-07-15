class Solution:
     def hasAlternatingBits(self, n):
         """
         :type n: int
         :rtype: bool
         """
         prev = n % 2
         n = n // 2
         while n > 0:
             now = n % 2
             if now == prev:
                 return False
             n = n // 2
             prev = now
         return True
