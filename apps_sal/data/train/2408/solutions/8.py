class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         letters = "abcdefghijklmnopqrstuvwxyz"
         unique = [s.index(l) for l in letters if s.count(l) == 1]
         return -1 if len(unique) == 0 else min(unique)

