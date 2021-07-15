class Solution:
     def validPalindrome(self, s):
         """
         :type s: str
         :rtype: bool
         """
         if s == s[::-1]:
             return True
 
         i,j =  0, len(s)-1
         while i < j:
             if s[i] == s[j]:
                 i+=1
                 j-=1
             else:
                 remove_i = s[:i] + s[i+1:]
                 remove_j = s[:j] + s[j+1:]
 
                 return remove_i == remove_i[::-1] or remove_j == remove_j[::-1]
