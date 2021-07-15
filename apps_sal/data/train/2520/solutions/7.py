class Solution:
     def reverse(self, x):
         """
         :type x: int
         :rtype: int
         """
         sign = 1
         if x<0:
             x=-x
             sign = -1
         result = 0
         while x>0:
             end = x%10
             result = result*10 + end
             x = x//10
         result *= sign
         if result > 2**31-1 or result < -2**31:
             return 0
         else:
             return result
