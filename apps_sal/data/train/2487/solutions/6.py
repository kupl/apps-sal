class Solution:
     def repeatedSubstringPattern(self, s):
         """
         :type s: str
         :rtype: bool
         """
         n = len(s)                  # find len
         for i in range(n//2,0,-1):  # loop from end to start
             if n%i ==0:             # if n is sub_len integer tiems
                 repeat = s[0:i]
                 if repeat*(n//i) ==s: #if repeat*several_times == s
                     return True
         return False
 

