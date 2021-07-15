class Solution:
     def isIsomorphic(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         """
    #    my second solution...modified based on first solution...
         l = len(s)
         
         sdic = {}
         snum = []
         i = 0
         j = 1
         while i < l:
             if s[i] not in sdic:
                 sdic[s[i]] = j
                 snum.append(j)
                 j += 1
             else:
                 snum.append(sdic[s[i]])
             i += 1
             
         tdic = {}
         tnum = []
         i = 0
         j = 1
         while i < l:
             if t[i] not in tdic:
                 if j != snum[i]:
                     return False
                 tdic[t[i]] = j
                 tnum.append(j)
                 j += 1
             else:
                 if tdic[t[i]] != snum[i]:
                     return False
                 tnum.append(tdic[t[i]])
             i += 1
         
         return True
         
         
         """
    #    my first solution...
         sdic = {}
         snum = []
         i = 0
         j = 1
         while i < len(s):
             if s[i] not in sdic:
                 sdic[s[i]] = j
                 snum.append(j)
                 j += 1
             else:
                 snum.append(sdic[s[i]])
             i += 1
             
         tdic = {}
         tnum = []
         i = 0
         j = 1
         while i < len(t):
             if t[i] not in tdic:
                 tdic[t[i]] = j
                 tnum.append(j)
                 j += 1
             else:
                 tnum.append(tdic[t[i]])
             i += 1
             
         if snum == tnum:
             return True
         else:
             return False

