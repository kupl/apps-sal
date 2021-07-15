class Solution:
     def checkRecord(self, s):
         if not s:
             return
         c=0
         if s=="AA":
             return False
         for i in range(len(s)-2):
             if s[i]=="L":
                 if s[i]==s[i+1] and s[i]==s[i+2]:
                     return False
             if s[i]=="A":
                 c+=1
                 if c==2:
                     return False
 
         return True
