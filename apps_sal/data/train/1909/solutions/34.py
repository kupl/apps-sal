class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ylen, xlen = len(grid), len(grid[0])
        rights = [[0 for i in range(xlen)] for j in range(ylen)]
        downs = [[0 for i in range(xlen)] for j in range(ylen)]
        for y in range(ylen - 1, -1, -1):
            for x in range(xlen - 1, -1, -1):
                if y < ylen - 1 and grid[y + 1][x] == 1:
                    downs[y][x] = downs[y + 1][x] + 1
                if x < xlen - 1 and grid[y][x + 1] == 1:
                    rights[y][x] = rights[y][x + 1] + 1
        ans = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    ans = max(ans, 1)
                    offset = 1
                    while y + offset < ylen and x + offset < xlen:
                        cury, curx = y + offset, x + offset
                        if grid[cury][x] == 1 and grid[y][curx] == 1:
                            if rights[cury][x] >= offset and downs[y][curx] >= offset:
                                ans = max(ans, 1 + offset)
                        else:
                            break
                        offset += 1
        return ans**2
