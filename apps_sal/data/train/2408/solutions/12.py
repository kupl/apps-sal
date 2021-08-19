class Solution:

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = set(s)
        l = [s.index(i) for i in a if s.count(i) == 1]
        if len(l) == 0:
            return -1
        else:
            return min(l)
