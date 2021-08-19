class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for w in s:
            if w not in dict:
                dict[w] = 1
            else:
                dict[w] += 1
        f = 0
        rlen = 0
        for w in dict:
            if not dict[w] % 2:
                rlen += dict[w]
            else:
                if not f:
                    rlen += 1
                rlen += dict[w] - 1
                f = 1
        return rlen
