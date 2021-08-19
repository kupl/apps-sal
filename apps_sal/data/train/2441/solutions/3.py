class Solution:

    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        for i in range(len(s) - 2, -1, -1):
            if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
                s = s[:i] + s[i + 2:]
                return self.makeGood(s)
        return s
