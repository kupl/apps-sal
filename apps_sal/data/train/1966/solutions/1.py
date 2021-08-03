class Solution:
    def numSubmat(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = 0
        heights = [0] * (n + 1)
        for x in range(m):
            stack = []
            dp = [0] * (n + 1)
            for y in range(n):
                if matrix[x][y] == 1:
                    heights[y] = heights[y] + 1
                else:
                    heights[y] = 0
            for right in range(n + 1):
                while stack and heights[right] <= heights[stack[-1]]:
                    cur = stack.pop()
                if stack:
                    left = stack[-1]
                    dp[right] = dp[left] + heights[right] * (right - left)
                else:
                    left = -1
                    dp[right] = heights[right] * (right - left)
                stack.append(right)
            res += sum(dp)
        return res
