class Solution:

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set(s)
        index = [s.index(l) for l in chars if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
