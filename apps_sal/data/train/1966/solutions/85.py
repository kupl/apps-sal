class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m-1):
                if mat[i][j+1]:
                    mat[i][j+1] += mat[i][j]

        ans = 0

        for j in range(m):
            for i in range(n):
                add = mat[i][j]
                for k in range(i, n):
                    add = min(add, mat[k][j])
                    ans += add

        return ans
