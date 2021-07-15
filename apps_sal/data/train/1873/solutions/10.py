class Solution:
     def canTransform(self, start, end):
         """
         :type start: str
         :type end: str
         :rtype: bool
         """
         tmps = start.replace("X","")
         tmpe = end.replace("X","")
         if tmps != tmpe:
             return False
         sa, ta = [], []
         i = 0
         while (i < len(start)):
             if start[i] == "L":
                 sa.append(i)
             elif start[i] == "R":
                 sa.append(-i)
             if end[i] == "L":
                 ta.append(i)
             elif end[i] == "R":
                 ta.append(-i)
             i += 1
         i = 0
         while(i < len(sa)):
             if sa[i]<ta[i]:
                 return False
             i += 1
         return True
