class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        left = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, len(left)):
            for j in range(1, len(left[0])):
                if mat[i - 1][j - 1] == 1:
                    left[i][j] = left[i][j - 1] + 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                minlen = float('inf')
                for k in range(i, -1, -1):
                    minlen = min(minlen, left[k + 1][j + 1])
                    res += minlen
        return res
