class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def flip(row):
            return [1 - r for r in row]

        record = dict()
        for row in matrix:
            record[tuple(row)] = record.get(tuple(row), 0) + 1
            record[tuple(flip(row))] = record.get(tuple(flip(row)), 0) + 1
        return max(record.values())
