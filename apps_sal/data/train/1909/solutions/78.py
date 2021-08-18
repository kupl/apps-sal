class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        top, left = copy.deepcopy(grid), copy.deepcopy(grid)

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    if i > 0:
                        top[i][j] = top[i - 1][j] + 1
                    if j > 0:
                        left[i][j] = left[i][j - 1] + 1

        ans = 0
        for s in range(min(R, C), 0, -1):
            for i in range(R - s + 1):
                for j in range(C - s + 1):
                    if min(top[i + s - 1][j], top[i + s - 1][j + s - 1], left[i][j + s - 1], left[i + s - 1][j + s - 1]) >= s:
                        return s * s

        return 0
