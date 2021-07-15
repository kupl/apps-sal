import math
 class Solution:
     def reachNumber(self, target):
         """
         :type target: int
         :rtype: int
         """
         nTarget = target if (target>0) else -target
         n = math.ceil((-1 + math.sqrt(1+8*nTarget))/(2))
         curSum = int(n*(n+1)/2)
         if curSum == nTarget: return n
         res = curSum - nTarget
         if res%2 == 0: return n
         if n%2 == 1: return n+2
         return n+1
