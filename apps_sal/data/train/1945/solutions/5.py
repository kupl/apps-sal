class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = {}
        for row in matrix:
            key = tuple(x ^ row[0] for x in row)
            counter[key] = counter.get(key, 0) + 1
        return max(counter.values())
