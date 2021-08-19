class Solution:

    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if i != len(s) - 1:
                t = self.calcScore(s[:i + 1], s[i + 1:])
                res = max(res, t)
        return res

    def calcScore(self, s1: str, s2: str) -> int:
        return s1.count('0') + s2.count('1')
