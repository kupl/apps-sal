class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        heights = [0] * m
        res = 0
        for i in range(0, n):
            stack = []
            count = 0
            for j in range(0, m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            for index, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    curr = stack.pop()
                    left = stack[-1] if stack else -1
                    count -= (heights[curr] - height) * (curr - left)
                count += height
                res += count
                stack.append(index)
        return res
            

