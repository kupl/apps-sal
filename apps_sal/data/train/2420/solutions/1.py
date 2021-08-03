class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ssort = sorted(list(s))
        tsort = sorted(list(t))
        return ssort == tsort
