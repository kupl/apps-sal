class Solution:
     def titleToNumber(self, s):
         """
         :type s: str
         :rtype: int
         """
         s = s[::-1]
         sum = 0
         for exp, char in enumerate(s):
             sum += (ord(char) - 65 + 1) * (26 ** exp)
         return sum
         

