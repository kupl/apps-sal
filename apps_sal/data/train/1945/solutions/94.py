from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = defaultdict(int)
        for row in matrix:
            ori = []
            inverse =[]
            for c in row:
                ori.append(str(c))
                inverse.append(str(1 - c))
            d[''.join(ori)] += 1
            d[''.join(inverse)] += 1
        lis = list(d.values())
        return max(lis)

