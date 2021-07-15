class Solution:
     def hasAlternatingBits(self, n):
         """
         :type n: int
         :rtype: bool
         """
         res = []
         while n > 0:
             res.append(str(n % 2))
             n //= 2
         for i in range(1, len(res)):
             if res[i] == res[i - 1]:
                 return False
         return True

