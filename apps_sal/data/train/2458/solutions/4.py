class Solution:

    def balancedStringSplit(self, s: str) -> int:
        (n, c) = (0, 0)
        for v in s:
            if v == 'R':
                n += 1
            else:
                n -= 1
            if n == 0:
                c += 1
        return c
