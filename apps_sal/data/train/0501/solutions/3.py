class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = "".join(list(reversed(s)))

        for i in range(len(s), 0, -1):
            if s[:i] == reversed_s[(len(s) - i):]:
                return reversed_s[:(len(s) - i)] + s

        return ""
