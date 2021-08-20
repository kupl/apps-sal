class Solution:

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def cnt(S):
            c = {}
            for i in S:
                if i in c:
                    c[i] += 1
                else:
                    c[i] = 1
            return c
        c1 = cnt(s)
        c2 = cnt(t)
        return c2 == c1
