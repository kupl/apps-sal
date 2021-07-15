import math
 class Solution:
     def smallestGoodBase(self, n):
         n = int(n)
         maxLength = int(math.log(n,2))
         for m in range(maxLength, 1, -1):
             k = int(n**m**-1)
             if (k**(m+1) - 1)//(k - 1) == n:
                 return str(k)
         return str(n-1)
         """
         :type n: str
         :rtype: str
         """
         
