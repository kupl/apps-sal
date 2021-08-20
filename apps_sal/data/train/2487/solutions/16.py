class Solution:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        base = 1
        while base <= length // 2:
            if length % base == 0:
                if s[:base] * (length // base) == s:
                    return True
            base += 1
        return False
