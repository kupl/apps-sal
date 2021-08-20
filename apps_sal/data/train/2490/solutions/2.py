import functools


class Solution:

    def gen_array(self, n, s):
        for x in range(n):
            yield (s + x * 2)

    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(lambda a, b: a ^ b, self.gen_array(n, start))
