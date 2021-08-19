class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = collections.Counter()
        flipper = {1: 0, 0: 1}
        for row in matrix:
            if row[0] == 0:
                row = [flipper[col] for col in row]
            counter[tuple(row)] += 1
        return max(counter.values())
