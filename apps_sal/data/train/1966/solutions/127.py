class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        res = 0
        for top in range(M):
            h = [1 for _ in range(N)]
            for bottom in range(top, M):
                for j in range(N):
                    h[j] &= mat[bottom][j]
                res += self.count1D(h)
        return res
    
    def count1D(self, array):
        res, length = 0, 0
        for i in range(len(array)):
            if array[i] == 0:
                length = 0
            else:
                length += 1
            res += length
        return res
