class Solution:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any((s[:i] * (len(s) // i) == s for i in range(1, len(s) // 2 + 1) if len(s) % i == 0))
