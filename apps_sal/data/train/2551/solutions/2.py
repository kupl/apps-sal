class Solution:
     
     import re
     
     def isValid(self, s):
         """
         :type s: str
         :rtype: bool
         """
         
         while(s!=""):
             len_orig = len(s)
             s = s.replace('()', '')
             s = s.replace('[]', '')
             s = s.replace('{}', '')
             if len(s) == len_orig:
                 return False
     
         return True
             

