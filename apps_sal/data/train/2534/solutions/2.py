class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            left_count = list(s[:i]).count('0')
            right_count = list(s[i:]).count('1')
            if left_count + right_count > res:
                res = left_count + right_count
        return res
