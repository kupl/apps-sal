class Solution:
     def checkRecord(self, s):
         """
         :type s: str
         :rtype: bool
         """
         aCount=0
         clCount=0
         for r in s:
             if r=='A':
                 aCount+=1
                 if aCount >1:
                     return False
             if r=='L':
                 clCount+=1
                 if clCount>2:
                     return False
             else:
                 clCount=0
         return True
