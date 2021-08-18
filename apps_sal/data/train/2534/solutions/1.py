class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        for i in range(len(s) - 1):
            s1 = s[:i + 1]
            i1 = list(s1).count('0')
            s2 = s[i + 1:]
            i2 = list(s2).count('1')
            total = i1 + i2
            if total >= maxi:
                maxi = total
        return maxi
