class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        i, j = 0, len(s) - 1
        dele = 1
        while i < j:
            if s[i] == s[j]:
                i, j = i + 1, j - 1
            else:
                t1, t2 = s[i + 1:j + 1], s[i:j]
                return t1 == t1[::-1] or t2 == t2[::-1]
        return True
