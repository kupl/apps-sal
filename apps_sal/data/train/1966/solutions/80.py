class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        (m, n) = (len(mat), len(mat[0]))
        res = 0
        for i in range(m):
            for j in range(n):
                if j:
                    if mat[i][j]:
                        mat[i][j] = mat[i][j - 1] + 1
        print(mat)
        for i in range(m):
            for j in range(n):
                ans = mat[i][j]
                for k in range(i, m):
                    ans = min(ans, mat[k][j])
                    res += ans
        return res
