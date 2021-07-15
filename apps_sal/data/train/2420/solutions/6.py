class Solution:
     def isAnagram(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         S = set(s)
         T = set(t)
         if len(s) != len(t):
             return False
         for i in T:
             if i in S:
                 if s.count(i) != t.count(i):
                     return False
             else:
                 return False
         return True

