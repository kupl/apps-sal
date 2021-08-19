class Solution:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        for i in range(1, size // 2 + 1):
            if size % i:
                continue
            if s[:i] * (size // i) == s:
                return True
        return False
