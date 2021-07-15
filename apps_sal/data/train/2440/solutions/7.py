class Solution:
     def climbStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         if n<=3:
             return n
 
         v=[1,2,3]
         for i in range(3,n):
             v.append(v[-1]+v[-2])
         return v[-1]
