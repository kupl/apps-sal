class Solution:
     def repeatedSubstringPattern(self, s):
         return s in (s + s)[1:-1]

