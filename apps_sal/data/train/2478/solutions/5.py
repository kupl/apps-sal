class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in set(t):
            if i not in set(s) or t.count(i) > s.count(i):
                return i
