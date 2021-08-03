class Solution:
    def helper(self, heights, n):
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev = stack[-1]
                res[i] = res[prev] + heights[i] * (i - prev)
            else:
                res[i] = heights[i] * (i + 1)
            stack.append(i)
        return sum(res)

    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [[0] * n for _ in range(m)]
        res = 0
        for j in range(n):
            if mat[0][j] == 1:
                heights[0][j] = 1
        for i in range(1, m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i - 1][j] + 1
        for i in range(m):
            res += self.helper(heights[i], n)
        return res
