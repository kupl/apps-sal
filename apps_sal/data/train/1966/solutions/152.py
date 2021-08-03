class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        # precipitate mat to histogram
        for r in range(m):
            for c in range(n):
                if mat[r][c] and r > 0:
                    mat[r][c] += mat[r - 1][c]  # histogram

        res = 0
        for r in range(m):
            stack = []  # mono-stack of indices of non-decreasing height for current row
            dp = 0  # number of submatrices with all 1's ending at (r,c-1) so far
            for c in range(n):
                while stack and mat[r][stack[-1]] > mat[r][c]:
                    start = stack.pop()  # start
                    end = stack[-1] if stack else -1  # end
                    # difference in height between the taller bar and the current bar * width to bar before taller bar
                    dp -= (mat[r][start] - mat[r][c]) * (start - end)  # adjust to reflect lower height

                dp += mat[r][c]  # count submatrices bottom-right at (i, j)
                res += dp
                stack.append(c)

        return res
