class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        record = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            record[str(vals)] += 1
            record[str(trans)] += 1
        return max(record.values())
