class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        m = len(mat)
        n = len(mat[0])

        for y in range(m):
            for x in range(n):
                if mat[y][x] and y > 0:
                    mat[y][x] += mat[y - 1][x]

        ans = 0
        for y in range(m):
            stack = []
            cnt = 0
            for x in range(n):
                while stack and mat[y][stack[-1]] > mat[y][x]:

                    prev_hist_end = stack.pop()
                    prev_hist_start = stack[-1] if stack else -1
                    cnt -= (prev_hist_end - prev_hist_start) * (mat[y][prev_hist_end] - mat[y][x])
                cnt += mat[y][x]
                ans += cnt
                stack.append(x)

        return ans
