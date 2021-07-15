class Solution:
     def hasAlternatingBits(self, n):
         """
         :type n: int
         :rtype: bool
         """
         before = None
         while n != 0:
             d = n%2
             if not before:
                 before = d + 1
             else:
                 if before == d + 1:
                     return False
                 before = d + 1
             n = n >> 1
             
         return True

