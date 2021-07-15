class Solution:
     def smallestGoodBase(self, n):
         """
         :type n: str
         :rtype: str
         """
         import math
         n=int(n)
         max_m=int(math.log2(n))
         
         for m in range(max_m,1,-1):
             
             k=int(n**(m**(-1)))
             if n==(k**(m+1)-1)//(k-1):
                return str(k)
         return str(n-1)
