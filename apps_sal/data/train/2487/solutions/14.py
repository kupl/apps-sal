class Solution:
     def repeatedSubstringPattern(self, s):
         """
         :type s: str
         :rtype: bool
         """
         s_len = len(s)
         for i in range(1,(s_len)//2+1):
             if s[i] == s[0]:
                 s_sub = s[:i]
                 s_new = s_sub * (s_len // i)
                 if s_new == s:
                     return True
         return False
