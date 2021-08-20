class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for start in range(0, len(s), 2 * k):
            p1 = start
            p2 = p1 + k - 1
            if p2 >= len(s):
                p2 = len(s) - 1
            while p1 < p2:
                (s[p1], s[p2]) = (s[p2], s[p1])
                p1 += 1
                p2 -= 1
        result = ''
        for ele in s:
            result += ele
        return result
