class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.rstrip()
        s = s.lstrip()
        for i in range(0, len(s))[::-1]:
            if s[i] == ' ':
                return len(s) - 1 - i
        return len(s)
