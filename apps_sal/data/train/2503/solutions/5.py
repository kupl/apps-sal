class Solution:

    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        m = len(a)
        n = len(b)
        if m != n:
            return max(m, n)
        elif a != b:
            return m
        else:
            return -1
