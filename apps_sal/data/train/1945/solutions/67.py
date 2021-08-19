class Solution:

    def flip_row(self, row):
        for (i, val) in enumerate(row):
            row[i] = row[i] ^ 1
        return row

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        seen = defaultdict(int)
        for (i, row) in enumerate(matrix):
            if tuple(row) in seen or tuple(self.flip_row(row)) in seen:
                seen[tuple(row)] += 1
            else:
                seen[tuple(row)] += 1
        result = 0
        for val in seen.values():
            result = max(result, val)
        return result
