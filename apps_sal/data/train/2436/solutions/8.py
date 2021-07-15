class Solution:
     def isPalindrome(self, s):
         """
         :type s: str
         :rtype: bool
         """
         s = s.lower()
         i = 0
         j = len(s) - 1
         while i < j:
             if not self._is_alphanumeric(s[i]):
                 i += 1
                 continue
             if not self._is_alphanumeric(s[j]):
                 j -= 1
                 continue
             if s[i] != s[j]:
                 return False
             i += 1
             j -= 1
         return True
 
     def _is_alphanumeric(self, c):
         if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
             return True
