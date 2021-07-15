class Solution:
     def countSegments(self, s):
         """
         :type s: str
         :rtype: int
         """
         c=0
         l=s.split(" ")
         for i in l:
             if i!="":
                 c+=1
         return c
