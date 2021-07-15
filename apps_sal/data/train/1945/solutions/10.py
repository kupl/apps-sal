class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        values = {}
        for row in matrix:
            s1, s2 = '', ''
            for c in row:
                s1 += str(c ^ 0)
                s2 += str(c ^ 1)
            print((s1, s2))
            values[s1] = values.get(s1, 0) + 1
            values[s2] = values.get(s2, 0) + 1
        return max(values.values())

