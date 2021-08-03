
from collections import defaultdict, deque


def gen_perm(n):
    if n == 1:
        return [0, 1]
    else:
        gen_prev = gen_perm(n - 1)
        right = [2 ** (n - 1) + num for num in gen_prev]
        return gen_prev + list(reversed(right))


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        perm = gen_perm(n)
        i = 0
        while perm[i] != start:
            i += 1
        return perm[i:] + perm[:i]
