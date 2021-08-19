from itertools import chain


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        start_mask = start
        while start_mask:
            start_mask >>= 1
            start ^= start_mask
        out = [x ^ (x >> 1) for x in chain(range(start, 2 ** n), range(start))]
        # print(out)
        return out
