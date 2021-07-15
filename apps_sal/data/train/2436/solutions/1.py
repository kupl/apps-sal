class Solution:
     def isPalindrome(self, s):
         """
         :type s: str
         :rtype: bool
         """
         s = s.lower()
         s = [c for c in s if c.isalnum()]
         return s == s[::-1]

