class Solution:

    def maxPower(self, s: str) -> int:
        z = []
        c = 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c = c + 1
            else:
                z.append(c)
                c = 0
        z.append(c)
        return max(z) + 1
