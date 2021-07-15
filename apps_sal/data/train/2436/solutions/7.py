class Solution:
     def isPalindrome(self, s):
         """
         :type s: str
         :rtype: bool
         """
         i = 0
         j = len(s) - 1
         while(i < j):
             while(i <= len(s) - 1 and not s[i].isalnum()):
                 i += 1
             while(j >= 0 and not s[j].isalnum()):
                 j -= 1
 
             if i < j and s[i].lower() != s[j].lower():
                 return False
 
             i += 1
             j -= 1
         return True

