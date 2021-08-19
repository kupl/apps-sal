class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ma = 0
        for i in matrix:
            c = matrix.count(i) + matrix.count([1 - x for x in i])
            if c > ma:
                ma = c
        return ma
