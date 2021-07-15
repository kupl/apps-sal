class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         
         letters='abcdefghijklmnopqrstuvwxyz'
         
         list = [ l for l in letters if s.count(l) == 1]
         
         for i in range(0, len(s)):
             if s[i] in list:
                 return i
             
         return -1
