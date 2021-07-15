from itertools import groupby
 class Solution:
     def reorganizeString(self, s):
         """
         :type d: str
         :rtype: str
         """
         counts = sorted([s.count(x) for x in set(s)] + [0])[::-1]
         
         if counts[0] > sum(counts[1:]) + 1:
             return ""
         
         gl = sorted([list(j) for i, j in groupby(sorted(list(s)))], key=lambda x: -len(x))
         
         res = ""
         while gl:
             
             res += gl[0].pop()
             if len(gl) > 1:
                 res += gl[1].pop()
 
             gl = list(filter(None, gl))
             gl.sort(key=lambda x: -len(x))
         return res
         
         
