class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        def countOneRow(A):
            res, length = 0, 0
            for a in A:
                length =  0 if a == 0 else length + 1
                res += length
            return res

        res, M, N = 0, len(mat), len(mat[0])
        
        for up in range(M):
            onesCol = [1] * N
            for down in range(up, M):
                for i in range(N):
                    onesCol[i] &= mat[down][i]
                res += countOneRow(onesCol)
        return res
                
            

