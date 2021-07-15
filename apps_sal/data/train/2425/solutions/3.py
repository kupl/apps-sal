class Solution:
     def countSegments(self, s):
         """
         :type s: str
         :rtype: int
         """
         count = 0
         finished = True
         for c in s:
             if finished:
                 if c is " ": continue
                 else:
                     finished = False
                     count += 1
             else:
                 if c is " ":
                     finished = True
                 else:
                     continue
         return count

