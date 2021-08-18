class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        res = 0

        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j]:
                    if j > 0:
                        mat[i][j] = mat[i][j - 1] + 1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    r = i
                    wid = mat[i][j]
                    while r < len(mat) and mat[r][j]:
                        wid = min(mat[r][j], wid)
                        res += wid
                        r += 1
        return res
