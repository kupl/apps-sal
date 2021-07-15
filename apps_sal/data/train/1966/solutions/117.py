class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        res = 0
        for up in range(M):
            h = [1 for i in range(N)]
            for down in range(up, M):
                for col in range(N):
                    h[col] &= mat[down][col]
                res += self.oneArray(h)
        return res
                
    
    def oneArray(self, arr):
        res = length = 0
        for a in arr:
            length = 0 if a == 0 else length + 1
            res += length
        return res
