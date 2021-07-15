class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        dp = [0] * n
        for r in range(m):
            stack = []
            for c in range(n):
                cnt = 0
                if mat[r][c]:
                    if r > 0:
                        mat[r][c] += mat[r-1][c]
                    while stack and mat[r][stack[-1]] >= mat[r][c]:
                        stack.pop()
                    cnt += (c - (stack[-1] if stack else -1))*mat[r][c]
                    if stack:
                        cnt += dp[stack[-1]]
                stack.append(c)
                dp[c] = cnt
                res += cnt
        return res
