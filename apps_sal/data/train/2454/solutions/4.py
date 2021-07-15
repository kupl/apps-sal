class Solution:
     def convertToTitle(self, n):
         res = ""
         while n != 0:
             tmp = (n-1)%26
             c = chr(ord("A") + tmp)
             res = c + res
             n = (n-1)//26
         return res
         """
         :type n: int
         :rtype: str
         """

