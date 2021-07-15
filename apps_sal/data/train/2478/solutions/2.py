class Solution:
     def findTheDifference(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: str
         """
         ss = sorted(s)
         st = sorted(t)
         i = 0 
         j = 0
         while i <= len(ss) - 1:
             if ss[i] == st[j]:
                 i += 1
                 j += 1
             else: return st[j]
         return st[j]
