from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        c = Counter()
        for row in matrix:
            c.update([tuple(row)])
            c.update([tuple(flip(row))])
        return max(c.values())


def flip(bits):
    return [1 if bit == 0 else 0 for bit in bits]
