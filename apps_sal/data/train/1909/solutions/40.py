class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        dp1 = [[0] * len(grid[0]) for i in range(len(grid))]
        dp2 = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                dp1[i][j] = (dp1[i - 1][j] if i - 1 >= 0 else 0) + 1
                dp2[i][j] = (dp2[i][j - 1] if j - 1 >= 0 else 0) + 1
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                for k in range(min(dp1[i][j], dp2[i][j]), 0, -1):
                    if k <= min(dp2[i - k + 1][j], dp1[i][j - k + 1]):
                        ret = max(ret, k**2)
                        break
        return ret
