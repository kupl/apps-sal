class Solution:
     def checkRecord(self, s):
         """
         :type s: str
         :rtype: bool
         """
         charA = charL = 0
         for c in s:
             if c == 'A':
                 charA += 1 
                 if charA > 1: return False
                 charL = 0
             elif c == 'L':
                 charL += 1
                 if charL > 2: return False
             else: 
                 charL = 0
             
         
         return True
         
             

