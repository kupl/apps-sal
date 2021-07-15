class Solution:
     def longestPalindrome(self, s):
         """
         :type s: str
         :rtype: int
         """
         re = 0
         set_s = set(s)
         flag = False
         for x in set_s:
             if s.count(x) % 2 == 0:
                 re += s.count(x)
             elif s.count(x) >= 3 :
                 re += s.count(x)-1
                 flag =True
             elif s.count(x) == 1:
                 flag =True
         if flag == True :
             re += 1
         return re
                 

