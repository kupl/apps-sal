class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        tot = 0
        for i in range(m):
            prev = []
            for j in range(n):
                if not mat[i][j]:
                    prev = []
                    continue
                if i > 0:
                    mat[i][j] += mat[i - 1][j]
                h = mat[i][j]
                tot += h
                for p in range(len(prev) - 1, -1, -1):
                    if prev[p] > h:
                        prev[p] = h
                    tot += prev[p]
                prev.append(h)
        return tot

