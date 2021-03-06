class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        left_ones = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    left_ones[i][j] = 0
                else:
                    left_ones[i][j] = 1
                    if j > 0:
                        left_ones[i][j] += left_ones[i][j - 1]
        res = 0
        for j in range(n):
            total = 0
            stack = []
            for i in range(m):
                height = 1
                total += left_ones[i][j]
                while stack and stack[-1][0] > left_ones[i][j]:
                    total -= stack[-1][1] * (stack[-1][0] - left_ones[i][j])
                    height += stack[-1][1]
                    stack.pop()
                res += total
                stack.append((left_ones[i][j], height))
        return res
