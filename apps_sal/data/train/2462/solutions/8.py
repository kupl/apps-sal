class Solution:
     def titleToNumber(self, s):
         """
         :type s: str
         :rtype: int
         """
         val = ord('A')
         length = len(s)
         sum = 0
         for i in range(length):
             sum = sum + (ord(s[i])-val+1)* 26**(length-1-i)
         return sum
