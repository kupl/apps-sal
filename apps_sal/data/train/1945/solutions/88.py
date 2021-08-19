from collections import defaultdict


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        mx = 1
        for row in matrix:
            ori = ''
            inverse = ''
            for c in row:
                ori += str(c)
                inverse += str(1 - c)
            d[ori] += 1
            d[inverse] += 1
            mx = max(mx, d[ori], d[inverse])
        return mx
