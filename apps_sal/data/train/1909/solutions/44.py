class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        up, left = [], []
        for _ in range(nrow):
            up.append([0] * ncol)
            left.append([0] * ncol)
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    if c - 1 >= 0:
                        left[r][c] = left[r][c - 1] + 1
                    else:
                        left[r][c] = 1
        for c in range(ncol):
            for r in range(nrow):
                if grid[r][c] == 1:
                    if r - 1 >= 0:
                        up[r][c] = up[r - 1][c] + 1
                    else:
                        up[r][c] = 1
        # print(left, up)

        ret = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 0:
                    continue
                for dist in range(0, min(r, c) + 1):

                    r2, c2 = r - dist, c - dist
                    # print(r, c, dist, r2, c2)
                    if grid[r2][c] == 0 or grid[r][c2] == 0:
                        break
                    if left[r2][c] >= dist + 1 and up[r][c2] >= dist + 1:
                        ret = max(ret, dist + 1)

        return ret ** 2
