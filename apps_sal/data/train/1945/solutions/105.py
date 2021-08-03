class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counts = defaultdict(int)

        for row in matrix:
            counts[tuple(row) if row[0] else tuple(x ^ 1 for x in row)] += 1

        return max(counts.values())
