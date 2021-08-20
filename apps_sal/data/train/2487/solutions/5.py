class Solution:

    def repeatedSubstringPattern(self, s):
        size = len(s)
        for x in range(1, size // 2 + 1):
            if size % x:
                continue
            if s[:x] * (size // x) == s:
                return True
        return False
