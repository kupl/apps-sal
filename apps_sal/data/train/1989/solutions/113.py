class Solution:
    def longestAwesome(self, s: str) -> int:
        memo = {0: -1}
        best = 0
        bitmap = 0
        for i, digit in enumerate(s):
            bitmap ^= 1 << int(digit)

            for j in range(10):
                key = bitmap ^ (1 << j)
                if key in memo:
                    best = max(best, i - memo[key])
            if bitmap not in memo:
                memo[bitmap] = i
            else:
                best = max(best, i - memo[bitmap])

        return best
