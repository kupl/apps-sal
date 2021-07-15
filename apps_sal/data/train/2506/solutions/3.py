class Solution:
     def isIsomorphic(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         from collections import defaultdict as dict
         if len(s) != len(t):
             return False
         if not s and not t:
             return True
         ssd = dict(lambda: 100)
         sst = dict(lambda: 100)
         for ss, tt in zip(s, t):
             if ssd[ss] == 100:
                 ssd[ss] = ord(ss) - ord(tt)
             if sst[tt] == 100:
                 sst[tt] = ord(tt) - ord(ss)
             if ssd[ss] == ord(ss) - ord(tt) and sst[tt] == ord(tt) - ord(ss):
                 continue
             else:
                 return False
         return True

