class Solution:
     # def canTransform(self, start, end):
     #     """
     #     :type start: str
     #     :type end: str
     #     :rtype: bool
     #     """
 
     def canTransform(self, start, end):
         # For (i, x) and (j, y) in enumerate(start), enumerate(end)
         # where x != 'X' and y != 'X',
         # and where if one exhausts early, it's elements are (None, None),...
         for (i, x), (j, y) in itertools.zip_longest(
                 ((i, x) for i, x in enumerate(start) if x != 'X'),
                 ((j, y) for j, y in enumerate(end) if y != 'X'),
                 fillvalue = (None, None)):
 
             # If not solid or accessible, return False
             if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                 return False
 
         return True
         
         
         # tmps = start.replace("X","")
         # tmpe = end.replace("X","")
         # if tmps != tmpe:
         #     return False
         # sa, ta = [], []
         # i = 0
         # while (i < len(start)):
         #     if start[i] == "L":
         #         sa.append(i)
         #     elif start[i] == "R":
         #         sa.append(-i)
         #     if end[i] == "L":
         #         ta.append(i)
         #     elif end[i] == "R":
         #         ta.append(-i)
         #     i += 1
         # i = 0
         # while(i < len(sa)):
         #     if sa[i]<ta[i]:
         #         return False
         #     i += 1
         # return True

