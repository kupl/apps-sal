# 753

from copy import deepcopy


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        ret = deepcopy(mat)
        m = len(mat)
        n = len(mat[0])

        @lru_cache(4)
        def row_sum(x, y):
            if not 0 <= x < m:
                return 0
            ret = 0
            for j in range(max(0, y), min(n, y + 2 * K + 1)):
                ret += mat[x][j]
            return ret

        @lru_cache(4)
        def col_sum(x, y):
            if not 0 <= y < n:
                return 0
            ret = 0
            for i in range(max(0, x), min(m, x + 2 * K + 1)):
                ret += mat[i][y]
            # print(\"colsum\", x, y, ret)
            return ret

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    t = 0
                    for u in range(0, min(K + 1, m)):
                        for v in range(0, min(K + 1, n)):
                            t += mat[u][v]
                    ret[0][0] = t
                    continue

                if i > 0:
                    ret[i][j] = ret[i - 1][j] - row_sum(i - 1 - K, j - K) + row_sum(i + K, j - K)
                else:
                    ret[i][j] = ret[i][j - 1] - col_sum(i - K, j - K - 1) + col_sum(i - K, j + K)

        return ret
