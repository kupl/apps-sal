class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        if len(s) == 1:
            return False
        for lenofsub in range(1, len(s)):
            if (len(s) % lenofsub == 0):
                substring = [s[0:lenofsub]] * (len(s) // lenofsub)
                if ''.join(substring) == s:
                    return True
        return False
