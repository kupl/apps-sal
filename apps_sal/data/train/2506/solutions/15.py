class Solution:

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for (a, b) in zip(s, t):
            if a not in d:
                if b in d.values():
                    return False
                else:
                    d[a] = b
            elif d[a] != b:
                return False
        return True
