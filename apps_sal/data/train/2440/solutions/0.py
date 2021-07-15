class Solution:
     
     dictionary = {}
     def climbStairs(self, n):
         """
         :type n: int
         :rtype: int
         """
         number = 0
         if n == 0 or n == 1:
             return 1
         if n in self.dictionary:
             return self.dictionary[n]
         else:
             number += self.climbStairs(n - 1) + self.climbStairs(n - 2)
             self.dictionary[n] = number
         return number
