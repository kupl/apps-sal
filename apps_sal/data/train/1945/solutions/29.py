class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = {}
        max_value = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            a = ''
            b = ''
            for j in range(m):
                if matrix[i][j] == 0:
                    a += str(j)
                else:
                    b += str(j)
            if a not in rows:
                rows[a] = 0
            if b not in rows:
                rows[b] = 0
            rows[a] += 1
            rows[b] += 1
            max_value = max(max_value, rows[a], rows[b])
        return max_value
