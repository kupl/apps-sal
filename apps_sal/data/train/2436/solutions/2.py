class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [symbol for symbol in s.lower() if 'a' <= symbol <= 'z' or '0' <= symbol <= '9']

        return s == s[::-1]
