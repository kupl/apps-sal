class Solution:

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return r + s
