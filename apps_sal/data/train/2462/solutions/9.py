class Solution:
     def titleToNumber(self, s):
         """
         :type s: str
         :rtype: int
         
         
         """
         s = s[::-1]
         res = 0
         for exp, c in enumerate(s):
             res += (ord(c)-65 + 1) * (26 ** exp)
         return res
