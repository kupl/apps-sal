class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ones = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                ones[i][j] += 1 + ones[i][j + 1]
        res = 0
        for i in range(n):
            for j in range(m):
                width = ones[i][j]
                for k in range(i, n):
                    width = min(width, ones[k][j])
                    res += width
        return res
