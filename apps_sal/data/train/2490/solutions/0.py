class Solution:

    def xorOperation(self, n: int, start: int) -> int:
        if n == 0:
            return 0
        i = 1
        res = start
        while i != n:
            res = res ^ 2 * i + start
            i += 1
        return res
