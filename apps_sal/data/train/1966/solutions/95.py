class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # 这道题是问有多少个submatrices有all ones
        # 和84Largest Rectangle in Histogram很像

        # 解法1 - 枚举右下角, 但是要先准备一个row_left_ones的矩阵方便快速查找
        m, n = len(mat), len(mat[0])
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

        #=================分割线=================#

        # 解法2 - 单调递增栈(从上往下，即遍历行i的顺序)
        res = 0
        for j in range(n):
            total = 0
            # stack里存两个信息：
            # 1. ij位置上的左1数目(height)
            # 2. 当前的宽度(实际上是垂直的高度, 我们相当于横着看)
            stack = []
            for i in range(m):
                total += left_ones[i][j]
                width = 1
                while stack and stack[-1][0] > left_ones[i][j]:
                    # 弹出的时候要减去多余的答案
                    last_ones, last_width = stack.pop()
                    # last_ones - left_ones[i][j] 看成多余的列数（比如多余5列）
                    # 这5列都和当前的右下角(i, j)能构成5个虚假的矩形
                    # 所以要减掉
                    total -= last_width * (last_ones - left_ones[i][j])
                    width += last_width
                res += total
                stack.append((left_ones[i][j], width))

        return res
