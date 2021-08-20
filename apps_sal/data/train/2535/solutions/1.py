class Solution:

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        for i in range(int(len(s) / 2)):
            if s[i] != s[-1 - i]:
                s1 = s[:i] + s[i + 1:]
                if s1 == s1[::-1]:
                    return True
                s2 = s[:-1 - i] + s[len(s) - i:]
                if s2 == s2[::-1]:
                    return True
                return False
