class Solution:

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        if l != len(t):
            return False
        d = {}
        for (i, letter) in enumerate(s):
            if letter not in d.keys():
                d[letter] = t[i]
            elif d[letter] != t[i]:
                return False
        d2 = {}
        for (i, letter) in enumerate(t):
            if letter not in d2.keys():
                d2[letter] = s[i]
            elif d2[letter] != s[i]:
                return False
        return True
