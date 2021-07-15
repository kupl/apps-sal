class Solution:
     def convertToTitle(self, num):
         res = []
         
         while num > 0:
             res.append(chr(ord('A') + (num - 1) % 26))
             num = (num - 1) // 26
         res.reverse()
         return "".join(res)
         
         """
         :type n: int
         :rtype: str
         """

