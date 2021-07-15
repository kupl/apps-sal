class Solution:
     def isIsomorphic(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         if len(s) != len(t): return False
         dic1, dic2 = {}, {}
         for i in range(len(s)):
             if s[i] in dic1 and dic1[s[i]] != t[i]:
                 return False
             if t[i] in dic2 and dic2[t[i]] != s[i]:
                 return False
             dic1[s[i]] = t[i]
             dic2[t[i]] = s[i]
         return True
