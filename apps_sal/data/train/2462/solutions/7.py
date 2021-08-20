class Solution:

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [ord(c) - 64 for c in s]
        result = 0
        x = len(s) - 1
        for i in range(0, len(s)):
            result += s[x - i] * 26 ** i
        return result
