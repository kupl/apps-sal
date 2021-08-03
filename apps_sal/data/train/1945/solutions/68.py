class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = collections.Counter()
        for row in matrix:
            patterns[tuple(row)] += 1
            flip = [1 - c for c in row]
            patterns[tuple(flip)] += 1
        return max(patterns.values())
