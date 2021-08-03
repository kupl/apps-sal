class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        left = []
        right = []
        up = []
        down = []
        for i in range(len(grid)):
            left.append([0] * len(grid[0]))
            right.append([0] * len(grid[0]))
            up.append([0] * len(grid[0]))
            down.append([0] * len(grid[0]))
        for i in range(len(grid)):
            left[i][0] = grid[i][0]
            right[i][-1] = grid[i][-1]
            for j in range(1, len(grid[0])):
                if grid[i][j] == 1:
                    left[i][j] = left[i][j - 1] + 1
                if grid[i][len(grid[0]) - j - 1] == 1:
                    right[i][len(grid[0]) - j - 1] = right[i][len(grid[0]) - j] + 1
        for j in range(len(grid[0])):
            up[0][j] = grid[0][j]
            down[-1][j] = grid[-1][j]
            for i in range(1, len(grid)):
                if grid[i][j] == 1:
                    up[i][j] = up[i - 1][j] + 1
                if grid[len(grid) - 1 - i][j] == 1:
                    down[len(grid) - 1 - i][j] = down[len(grid) - i][j] + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left[i][j] = min(left[i][j], up[i][j])
                right[i][j] = min(right[i][j], down[i][j])
        maxium = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if right[i][j] != 0:
                    k = 1
                    while k <= right[i][j] and i + k - 1 < len(grid) and j + k - 1 < len(grid[0]):
                        if left[i + k - 1][j + k - 1] >= k:
                            maxium = max(maxium, k)
                        k += 1
        return maxium ** 2
