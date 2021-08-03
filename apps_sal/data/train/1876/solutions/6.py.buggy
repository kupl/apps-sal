import math
 class Solution:
     def reachNumber(self, x):
         """
         :type target: int
         :rtype: int
         """
         if x == 0:
             return 0
 
         x = abs(x)
         n = max(math.floor(math.sqrt(2 * x)) - 1, 0)
         sum = n * (n + 1) // 2
         while sum < x:
             n += 1
             sum += n
 
         if (sum - x) % 2 == 0:
             return n
         else:
             if (n + 1) % 2 == 1:
                 return n + 1
             else:
                 return n + 2
