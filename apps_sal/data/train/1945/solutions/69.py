class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # If all elements in serveral rows are the same after some number of flipping
        # Because we flip the whole columns, all the cells in one column will be changed
        # The rows should have the same opposite elements for those columns originally
        # So we can record the number of row before flipping and after flipping
        # The maximum number of rows is the answer
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
