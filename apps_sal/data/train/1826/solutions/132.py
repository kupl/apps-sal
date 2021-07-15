class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        def blockSum(x, y, vertical=K, horizontal=K):
            s = 0
            for i in range(x - vertical, x + vertical + 1):
                for j in range(y - horizontal, y + horizontal + 1):
                    if 0 <= i < n and 0 <= j < m:
                        s += mat[i][j]
            return s

        result = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            result[i][0] = blockSum(0, 0) if i == 0 \\
                else result[i - 1][0] \\
                     + (blockSum(i + K, 0, 0, K) if i < n - K else 0) \\
                     - (blockSum(i - (K + 1), 0, 0, K) if i >= K + 1 else 0)

            for j in range(1, m):
                result[i][j] = result[i][j - 1] \\
                               + (blockSum(i, j + K, K, 0) if j < m - K else 0) \\
                               - (blockSum(i, j - (K + 1), K, 0) if j >= K + 1 else 0)

        return result
