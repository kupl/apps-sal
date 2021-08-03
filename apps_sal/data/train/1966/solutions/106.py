class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])

        res = 0

        for i in range(M):
            r = [1] * N
            for j in range(i, M):
                r = [r[k] & mat[j][k] for k in range(N)]
                res += self.countOneRow(r)
        return res

    def countOneRow(self, r):
        res = length = 0
        for i, x in enumerate(r):
            length = 0 if x == 0 else length + 1
            res += length
        return res
