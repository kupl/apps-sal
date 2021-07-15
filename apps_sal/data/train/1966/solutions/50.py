class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        res = 0
        for up in range(r):
            ans = [1] * c
            for down in range(up, r):
                for j in range(c):
                    ans[j] = ans[j] & mat[down][j]
                res += self.cal(ans)
        return res
    
    def cal(self, ans):
        res = 0
        cur = 0
        n = len(ans)
        for i in range(n):
            if ans[i] == 0:
                cur = 0
            else:
                cur += 1
                res += cur
        return res
