class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        for r in range(m):
            for c in range(n):
                if mat[r][c] and r > 0:
                    mat[r][c] += mat[r - 1][c]
        res = 0
        for r in range(m):
            count = 0
            stack = []
            for c in range(n):
                while stack and mat[r][stack[-1]] > mat[r][c]:
                    j = stack.pop()
                    w = stack[-1] if stack else -1
                    count -= (mat[r][j] - mat[r][c]) * (j - w)
                count += mat[r][c]
                res += count
                stack.append(c)
        return res
