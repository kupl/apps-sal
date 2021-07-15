class Solution:
     def isIsomorphic(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         d = dict()
         for (a,b) in zip(s,t):
             # new mapping
             if a not in d:
                 # duplicates in t
                 if b in d.values():
                     return False
                 else:
                     d[a] = b
             # old mapping
             else:
                 # no duplicate in t
                 if d[a] != b:
                     return False
         return True
