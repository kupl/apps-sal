class Solution:

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        '\n         counter = 0\n         wasspace = 1\n         for char in s:\n             if char == " ":\n                 wasspace = 1\n                 continue\n             if wasspace == 1:\n                 counter += 1\n                 wasspace = 0\n         return counter\n         '
        return len(s.split())
