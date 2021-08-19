class Solution:

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = list(s)
        b = list(t)
        for c in s:
            a.remove(c)
            b.remove(c)
        return b[0]
