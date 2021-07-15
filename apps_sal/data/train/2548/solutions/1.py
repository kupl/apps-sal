class Solution:
     def isUgly(self, num):
         """
         :type num: int
         :rtype: bool
         """
         if num == 0:
             return False
         for d in (5, 3, 2):
             while num % d == 0:
                 num //= d
             if num == 1:
                 break
         else:
             return False
         return True

