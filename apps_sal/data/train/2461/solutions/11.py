class Solution:
     def isPowerOfTwo(self, n):
         """
         :type n: int
         :rtype: bool
         """
         
         if n < 0:
             return False
         
         if bin(n).replace('0b','').count('1') == 1:
             return True
         return False
