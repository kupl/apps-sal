class Solution:
    def maxScore(self, s: str) -> int:
        maxi = 0
        for i in range(1, len(s)):
            a = s[:i]
            b = s[i:]
            maxi = max(a.count('0') + b.count('1'), maxi)
        return maxi
