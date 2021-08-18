import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(collections.Counter(tuple(x ^ r[0] for x in r) for r in matrix).values())
