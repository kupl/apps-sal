class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        d = collections.defaultdict(int)
        (m, n) = (len(matrix), len(matrix[0]))
        for i in range(m):
            t1 = 0
            t2 = 0
            for j in range(n):
                t1 = ((t1 << 1) + matrix[i][j]) % mod
                t2 = ((t2 << 1) + 1 - matrix[i][j]) % mod
            d[t1] += 1
            d[t2] += 1
        return max(d.values())
