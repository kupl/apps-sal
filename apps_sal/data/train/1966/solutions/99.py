class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def countOneRow(a):
            res = 0
            length = 0
            for el in a:
                if el == 0:
                    length = 0
                else:
                    length += 1

                res += length
            return res
        
        M = len(mat)
        N = len(mat[0])
        res = 0
        for up in range(M):
            h = [1] * N
            for down in range(up, M):
                for k in range(N):
                    h[k] *= mat[down][k]
                print(h)
                res += countOneRow(h)
        return res

