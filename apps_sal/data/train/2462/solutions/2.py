class Solution:

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            res *= 26
            res += ord(i) - ord('A') + 1
        return res
