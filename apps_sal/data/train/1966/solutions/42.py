class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def oneDim(mat):
            res = 0
            length = 0
            for el in mat:
                if el == 0:
                    length = 0
                else:
                    length += 1
                res += length
            return res

        res = 0
        M = len(mat)
        N = len(mat[0])
        for top in range(M):
            h = [1] * N
            for bot in range(top, M):
                for i in range(N):
                    h[i] *= mat[bot][i]
                res += oneDim(h)

        return res
