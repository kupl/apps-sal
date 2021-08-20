class Solution:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                repeat = s[0:i]
                if repeat * (n // i) == s:
                    return True
        return False
