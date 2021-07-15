class Solution:
     def trailingZeroes(self, n):
         """
         :type n: int
         :rtype: int
         """
         c=0
         while n>0:
             n//=5
             c+=n
         return c

