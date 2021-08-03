class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = Counter()
        for r in matrix:
            normal = []
            reverse = []
            for v in r:
                normal.append(str(v))
                reverse.append(str(1 - v))
            d[''.join(normal)] += 1
            d[''.join(reverse)] += 1
        return max(d.values())
