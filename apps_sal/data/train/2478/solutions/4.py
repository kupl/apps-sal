class Solution:
     def findTheDifference(self, s, t):
         for i in t:
             if not i in s or t.count(i) != s.count(i):
                 return i

