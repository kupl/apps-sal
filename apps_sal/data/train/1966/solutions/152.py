class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        for r in range(m):
            for c in range(n):
                if mat[r][c] and r > 0:
                    mat[r][c] += mat[r - 1][c]
        res = 0
        for r in range(m):
            stack = []
            dp = 0
            for c in range(n):
                while stack and mat[r][stack[-1]] > mat[r][c]:
                    start = stack.pop()
                    end = stack[-1] if stack else -1
                    dp -= (mat[r][start] - mat[r][c]) * (start - end)
                dp += mat[r][c]
                res += dp
                stack.append(c)
        return res
