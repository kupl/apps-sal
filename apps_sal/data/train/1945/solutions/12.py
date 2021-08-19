class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        def find_minor(row):
            one = row.count(1)
            if one * 2 == len(row):
                return tuple((i for (i, val) in enumerate(row) if val == row[-1]))
            elif one * 2 > len(row):
                return tuple((i for (i, val) in enumerate(row) if val == 0))
            return tuple((i for (i, val) in enumerate(row) if val == 1))
        counts = collections.Counter()
        for (i, row) in enumerate(matrix):
            counts[find_minor(row)] += 1
        return max(counts.values())
