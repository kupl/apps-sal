class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 1:
                for j in range(n):
                    matrix[i][j] ^= 1
        cnt = Counter(list(map(tuple, matrix)))
        return max(cnt.values())

