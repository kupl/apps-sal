class Solution:
     def climbStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         if n <= 0:
             return 0
         if n==1:
             return 1
         if n==2:
             return 2
         a, b=1,2
         for i in range(n)[2:]:
             a,b=b,a+b
         return b

