import time


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ma = 0
        for i in matrix:
            flipped = [1 - j for j in i]
            c = matrix.count(i) + matrix.count(flipped)
            if c > ma:
                ma = c
        return ma
