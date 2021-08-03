class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        out = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val != 0:
                    cur_max = max_collect(x, y, grid)
                    out = max(out, cur_max)
        return out


def max_collect(x, y, grid, visited=set([])):
    if y < 0 or y >= len(grid):
        return 0
    if x < 0 or x >= len(grid[y]):
        return 0
    if grid[y][x] == 0:
        return 0
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    _max = 0
    for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        _max = max(_max, max_collect(xx, yy, grid, visited))
    visited.remove((x, y))
    return _max + grid[y][x]
