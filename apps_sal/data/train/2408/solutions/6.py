class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         letters = 'abcdefghijklmnopqrstuvwxyz'
         res = len(s)
         for x in letters:
             lInd = s.find(x)
             if lInd != -1 and lInd == s.rfind(x) and res > lInd:
                 res = lInd
         return -1 if len(s) == res else res
