class Solution:

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.split())
        a = ''
        for i in range(len(s)):
            if i + 1 < len(s):
                for j in range(len(s[i]) - 1, -1, -1):
                    a += s[i][j]
                a += ' '
            else:
                for j in range(len(s[i]) - 1, -1, -1):
                    a += s[i][j]
        return a
