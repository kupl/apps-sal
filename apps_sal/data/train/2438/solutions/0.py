class Solution:
     def lengthOfLastWord(self, s):
         """
         :type s: str
         :rtype: int
         """
         x = s.split()
         return len(x[-1]) if len(x) > 0 else 0
