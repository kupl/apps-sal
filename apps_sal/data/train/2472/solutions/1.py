class Solution:
     def checkRecord(self, s):
         twoL = 0
         twoA = 0
         i = 0
         while i < len(s):
             if s[i] == 'A':
                 twoA += 1
                 if twoA > 1:
                     return False
                 twoL = 0
             elif s[i] == 'L':
                 twoL += 1
                 if twoL > 2:
                     return False
             else:
                 twoL = 0
             i += 1
         return True
