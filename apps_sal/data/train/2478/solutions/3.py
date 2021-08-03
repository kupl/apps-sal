class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return [i for i in t if i not in s or s.count(i) != t.count(i)][0]
    # one more letter not more than one letter and rtype=return type --string
