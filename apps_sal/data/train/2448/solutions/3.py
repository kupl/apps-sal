class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = [False] * 58
        res = 0
        for x in s:
            t = ord(x) - 65
            if tmp[t]:
                res += 2
            tmp[t] = not tmp[t]
        if res != len(s):
            res += 1
        return res
