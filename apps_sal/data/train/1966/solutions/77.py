class Solution:
    def numSubmat(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for up in range(m):
            h = [1]*n
            for down in range(up, m):
                for k in range(n):
                    h[k] &= mat[down][k]
                res += self.countOneRow(h)
        return res

    def countOneRow(self, arr):
        res, length = 0, 0
        for i in range(len(arr)):
            length = 0 if arr[i]==0 else length+1
            res += length
        return res

