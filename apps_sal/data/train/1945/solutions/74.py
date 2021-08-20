class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = Counter()
        for r in matrix:
            normal = []
            reverse = []
            for v in r:
                normal.append('1' if v else '0')
                reverse.append('0' if v else '1')
            d[''.join(normal)] += 1
            d[''.join(reverse)] += 1
        return max(d.values())
