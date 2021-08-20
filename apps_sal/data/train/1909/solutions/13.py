class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        left = [[0 for j in range(n)] for i in range(m)]
        right = [[0 for j in range(n)] for i in range(m)]
        top = [[0 for j in range(n)] for i in range(m)]
        bottom = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i - 1][j] + 1
                    else:
                        top[i][j] = 1
                    if j:
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    if i == m - 1:
                        bottom[i][j] = 1
                    else:
                        bottom[i][j] = bottom[i + 1][j] + 1
                    if j == n - 1:
                        right[i][j] = 1
                    else:
                        right[i][j] = right[i][j + 1] + 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, 1)
                    side = min(left[i][j], top[i][j])
                    for k in range(side, 0, -1):
                        (x, y) = (i - k + 1, j - k + 1)
                        if right[x][y] >= k and bottom[x][y] >= k:
                            res = max(res, k ** 2)
                            break
        return res
