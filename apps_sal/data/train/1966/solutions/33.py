class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i - 1][j]

        res = 0
        for i in range(m):
            stack = []
            cnt = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    tmp = stack.pop()
                    left = stack[-1] if stack else -1
                    cnt -= (mat[i][tmp] - mat[i][j]) * (tmp - left)
                cnt += mat[i][j]
                res += cnt
                stack.append(j)
        return res
