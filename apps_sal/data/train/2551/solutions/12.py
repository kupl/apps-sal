class Solution:
     def isValid(self, s):
         while '()' in s or '{}' in s or '[]' in s:
             s = s.replace('{}','').replace('()','').replace('[]','')
         
         if s == '':
             return True
         else:
             return False
             
         """
         :type s: str
         :rtype: bool
         """

