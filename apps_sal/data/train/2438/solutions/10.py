class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        n_c = 0
        for i in range(l - 1, -1, -1):
            if s[i] != ' ':
                n_c += 1
            elif s[i] == ' ' and n_c == 0:
                pass
            elif s[i] == ' ' and n_c != 0:
                return n_c
        return n_c
