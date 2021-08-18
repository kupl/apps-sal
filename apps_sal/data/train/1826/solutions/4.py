class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def get_sum(i, j):
            ssum = 0
            for a in range(-K, K + 1):
                for b in range(-K, K + 1):
                    ssum += mat[i + a][j + b] if (0 <= (i + a) < m and 0 <= (j + b) < n) else 0
            return ssum

        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[i][j] = get_sum(0, 0)
                else:
                    if i == 0:
                        res[i][j] = res[i][j - 1] - sum([mat[b][j - K - 1] if (0 <= (j - K - 1) < n and 0 <= b < m) else 0 for b in range(i - K, i + K + 1)]) + sum([mat[b][j + K] if (0 <= (j + K) < n and 0 <= b < m) else 0 for b in range(i - K, i + K + 1)])
                    else:
                        res[i][j] = res[i - 1][j] - sum([mat[i - K - 1][b] if (0 <= (i - K - 1) < m and 0 <= b < n) else 0 for b in range(j - K, j + K + 1)]) + sum([mat[i + K][b] if (0 <= (i + K) < m and 0 <= b < n) else 0 for b in range(j - K, j + K + 1)])

        return res
