class Solution:
     def climbStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         
         # n[0] = 1
         # n[1] = 1
         # n[2] = n[0] + n[1]
         # n[3] = n[1] + n[2]
         # n[4] = n[2] + n[3]
         
         if n == 0 or n == 1:
             return 1
         
         ns = [1, 1]
         for i in range(2, n):
             ns[i%2] = sum(ns)
             
         return sum(ns)
         

