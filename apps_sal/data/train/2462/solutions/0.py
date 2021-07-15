class Solution:
     def titleToNumber(self, s):
         """
         :type s: str
         :rtype: int
         """
         r, t = 0, 1
         for i in s:
             r = r*26 +(ord(i)-64)
             #t *= 26
         return r
