# https://www.acwing.com/solution/LeetCode/content/3171/
# 找出边界全部由 1 组成的最大正方形子网格并返回该子网格中的元素数量
# 枚举每一个子正方形, 第一重循环枚举正方形的长度 length, 第二三重循环枚举左上角的顶点的 x 和 y 坐标位置
# 对于每个正方形, 在线性时间内判断它是否合法
# sum_row[i][j] 表示第 i 行前 j 列数字的和, sum_col[j][i] 表示第 j 列前 i 行的和, 因为是前缀和, 这里的 i 和 j 都从下标 1 开始
# 提前计算出 prefix sum 用于之后在线性复杂度内判断正方形是否合法 (判断四条边的区间和是不是等于 length)
# O(n ∗ m ∗ min(n, m)) time complexity, O(nm) space complexity
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sum_row, sum_col = [[0] * (m + 1) for _ in range(n + 1)], [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                sum_row[i][j] = sum_row[i][j - 1] + grid[i - 1][j - 1]
        for j in range(m + 1):
            for i in range(n + 1):
                sum_col[j][i] = sum_col[j][i - 1] + grid[i - 1][j - 1]
        
        for length in range(min(n, m), 0, -1):
            for i in range(n - length + 1):
                for j in range(m - length + 1):
                    x, y = i + length - 1, j + length - 1
                    if sum_row[i + 1][y + 1] - sum_row[i + 1][j] == length \\
                    and sum_row[x + 1][y + 1] - sum_row[x + 1][j] == length \\
                    and sum_col[j + 1][x + 1] - sum_col[j + 1][i] == length \\
                    and sum_col[y + 1][x + 1] - sum_col[y + 1][i] == length:
                        return length * length
        return 0

