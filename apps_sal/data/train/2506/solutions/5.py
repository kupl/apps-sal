class Solution:
     def isIsomorphic(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         map1 = {}
         map2 = {}
         for i in range(len(s)):
             if (s[i] in map1 and map1[s[i]] != t[i]) or (t[i] in map2 and map2[t[i]] != s[i]):
                 return False
             else:
                 map1[s[i]] = t[i]
                 map2[t[i]] = s[i]
         return True
