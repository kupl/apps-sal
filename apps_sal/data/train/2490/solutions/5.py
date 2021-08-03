class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        a = start

        for i in range(1, n):

            a = a ^ (start + 2 * i)

        return a
