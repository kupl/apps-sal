class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        for i, row in enumerate(matrix):
            matrix[i] = tuple(x ^ row[0] for x in row)
        return max(Counter(matrix).values())
