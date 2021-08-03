class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        r = s[::-1]
        for i in range(0, len(s)):
            if r[i] == s[i]:
                continue
            else:
                break
        r = r[:i] + r[i + 1:]
        if r == r[::-1]:
            return True
        s = s[:i] + s[i + 1:]
        return s == s[::-1]
