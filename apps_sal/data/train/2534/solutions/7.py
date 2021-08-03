class Solution:
    def maxScore(self, s: str) -> int:
        count = 0
        for i in range(1, len(s)):
            a, b = Counter(s[:i]), Counter(s[i:])
            count = max(count, a['0'] + b['1'])
        return count
