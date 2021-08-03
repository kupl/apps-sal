import collections
 
 
 def reorganize(s):
 
     counts = collections.Counter(s)
     output = []
     last_char = None
 
 
     while counts:
 
         for c, count in sorted(counts.items(), key=lambda x:x[1], reverse=True):
             if output and c == output[-1]:
                 if len(counts) == 1:
                     #  return "".join(output)
                     return ""
             else:
                 output.append(c)
                 counts[c] -= 1
                 if counts[c] == 0:
                     counts.pop(c)
                 break
 
     return "".join(output)
 
 
 
 class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         return reorganize(S)
