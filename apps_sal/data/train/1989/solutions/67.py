class Solution:
    def longestAwesome(self, s: str) -> int:
        memo = {0: -1}
        best = 0
        bitmap = 0
        for i, digit in enumerate(s):
            bitmap ^= (1 << int(digit))
            best = max(best, i - memo.get(bitmap, i))
            for j in range(10):
                key = bitmap ^ (1 << j)
                best = max(best, i - memo.get(key, i))
            memo[bitmap] = memo.get(bitmap, i)

        return best
