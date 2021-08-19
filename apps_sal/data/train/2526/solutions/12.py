class Solution:

    def trailingZeroes(self, n):
        return n // 5 + self.trailingZeroes(n // 5) if n >= 5 else 0
