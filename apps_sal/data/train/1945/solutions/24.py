class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        res = 0
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            count = 0
            flip = [0 for _ in range(m)]

            for j in range(m):
                flip[j] = 1 - matrix[i][j]

            for k in range(i, n):
                if matrix[k] == matrix[i] or matrix[k] == flip:
                    count += 1

            res = max(res, count)

        return res
