import math
 
 class Solution:
     def reachNumber(self, target):
         """
         :type target: int
         :rtype: int
         """
         if target < 0: target = - target
         n = math.floor((target * 2) ** 0.5)
         while n * (n + 1) < 2 * target: n += 1
         while ((n - 1) % 4) >> 1 == target % 2: n += 1
         return n
