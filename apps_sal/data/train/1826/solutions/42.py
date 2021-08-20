class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        (m, n) = (len(mat), len(mat[0]))
        if K >= max(m - 1, n - 1):
            return [[sum([sum(i) for i in mat])] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                res[r][c] = sum([sum(i[max(c - K, 0):min(n, c + K + 1)]) for i in mat[max(0, r - K):min(m, r + K + 1)]])
        return res
