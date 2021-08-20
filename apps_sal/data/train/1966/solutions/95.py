class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        row_left_ones = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    row_left_ones[i][j] = 0
                else:
                    row_left_ones[i][j] = 1
                    if j > 0:
                        row_left_ones[i][j] += row_left_ones[i][j - 1]
        res = 0
        for i in range(m):
            for j in range(n):
                curr_row_left_ones = row_left_ones[i][j]
                for k in range(i, -1, -1):
                    curr_row_left_ones = min(curr_row_left_ones, row_left_ones[k][j])
                    res += curr_row_left_ones
        return res
        res = 0
        for j in range(n):
            total = 0
            stack = []
            for i in range(m):
                total += left_ones[i][j]
                width = 1
                while stack and stack[-1][0] > left_ones[i][j]:
                    (last_ones, last_width) = stack.pop()
                    total -= last_width * (last_ones - left_ones[i][j])
                    width += last_width
                res += total
                stack.append((left_ones[i][j], width))
        return res
