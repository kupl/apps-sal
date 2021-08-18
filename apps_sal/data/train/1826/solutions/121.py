class Solution:

    def __init__(self):
        from functools import lru_cache
        return

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        self.cache = {}
        k = K
        n, m = len(mat), len(mat[0]) if len(mat) else 0

        def brute_force():
            def kernel(i, j, k):
                minx, maxx = max(i - k, 0), min(i + k + 1, n)
                miny, maxy = max(j - k, 0), min(j + k + 1, m)
                s = 0
                for ii in range(minx, maxx):
                    for jj in range(miny, maxy):
                        s += mat[ii][jj]
                return s

            ans = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    ans[i][j] = kernel(i, j, k)
            return ans

        def partials():
            @lru_cache
            def getrowsum(i, j, k):
                if i < 0:
                    return 0
                if i >= n:
                    return 0
                miny, maxy = max(j - k, 0), min(j + k + 1, m)
                return sum([mat[i][jj] for jj in range(miny, maxy)])

            def getcolsum(ans, i, j, k):
                if j < 0:
                    return 0
                if j >= m:
                    return 0
                minx, maxx = max(i - k, 0), min(i + k + 1, n)
                return sum([ans[ii][j] for ii in range(minx, maxx)])

            ans = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    ans[i][j] = getrowsum(i, j, k)

            res = [[0 for j in range(m)] for i in range(n)]
            for i in range(n):
                for j in range(m):
                    res[i][j] = getcolsum(ans, i, j, k)
            return res

        return partials()
