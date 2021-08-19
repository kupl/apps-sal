class Solution:

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        rev = s[::-1]
        for i in range(len(s)):
            if rev[i:] == s[:len(s) - i]:
                return rev[:i] + s
