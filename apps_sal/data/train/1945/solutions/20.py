class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = {}
        max_value = 0
        n = len(matrix)
        for i in range(n):
            if matrix[i][0] == 1:
                a = tuple(matrix[i])
            else:
                a = tuple([1 - c for c in matrix[i]])
            if a not in rows:
                rows[a] = 0
            rows[a] += 1

            max_value = max(max_value, rows[a])
        return max_value
