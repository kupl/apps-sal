class Solution:
     def isPowerOfFour(self, num):
         """
         :type num: int
         :rtype: bool
         """
         
         if num <= 0:
             return False
         
         import math
         i = math.log10(num) / math.log10(4)
         return i.is_integer()
