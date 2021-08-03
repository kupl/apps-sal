class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        maxVal = 0
        m = len(grid)
        n = len(grid[0])
        hor = [[0] * n for i in range(m)]
        ver = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = 1 if j == 0 else 1 + hor[i][j - 1]
                    ver[i][j] = 1 if i == 0 else 1 + ver[i - 1][j]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                small = min(hor[i][j], ver[i][j])
                while small > maxVal:
                    if ver[i][j - small + 1] >= small and hor[i - small + 1][j] >= small:
                        maxVal = small
                    small -= 1
        return maxVal**2
