class Solution:

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping1 = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mapping1.setdefault(s[i], None)
            if mapping1[s[i]] == None:
                mapping1[s[i]] = t[i]
            elif mapping1[s[i]] != t[i]:
                return False
        if len(set(mapping1.values())) == len(list(mapping1.values())):
            return True
        return False
