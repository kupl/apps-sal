class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        (rc, cc) = (len(mat), len(mat[0]))
        acc = [[0] * (cc + 1) for _ in range(rc + 1)]
        for r in range(rc):
            for c in range(cc):
                acc[r + 1][c + 1] = acc[r][c + 1] + acc[r + 1][c] - acc[r][c] + mat[r][c]
        res = [[0] * cc for _ in range(rc)]
        for r in range(rc):
            for c in range(cc):
                res[r][c] = acc[min(r + K + 1, rc)][min(c + K + 1, cc)] - acc[max(r - K, 0)][min(c + 1 + K, cc)] - acc[min(r + 1 + K, rc)][max(c - K, 0)] + acc[max(r - K, 0)][max(c - K, 0)]
        return res
