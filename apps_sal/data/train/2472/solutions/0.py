class Solution:
     def checkRecord(self, s):
         count = 0
         for i in range(0,len(s)):
             if s[i] == "A":
                 count += 1
                 if count == 2:
                     return False
             elif i >= 2 and s[i] == "L" and s[max(i-1,0)] == "L" and s[max(i-2,0)] == "L":
                 return False
         return True

