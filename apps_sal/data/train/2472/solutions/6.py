class Solution:
     def checkRecord(self, s):
         """
         :type s: str
         :rtype: bool
         """
         from collections import Counter
         val=Counter(s)
         idx=[]
         for i in range(len(s)):
             if s[i]=="L":
                 idx.append(i)
         for j in range(len(idx)-2):
             if idx[j+2]-idx[j]==2:
                 return False
             
         if val["A"]>1:
             return False
         return True
