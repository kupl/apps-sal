class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        gold = 0
        visited = [[False for y in range(b)] for x in range(a)]

        def maxgoldpath(x, y, visited):
            if (x < 0) or (x >= a) or (y < 0) or (y >= b) or (grid[x][y] == 0) or (visited[x][y]):
                return 0
            else:
                visited[x][y] = True
                left = maxgoldpath(x, y - 1, visited)
                right = maxgoldpath(x, y + 1, visited)
                top = maxgoldpath(x - 1, y, visited)
                down = maxgoldpath(x + 1, y, visited)
                visited[x][y] = False
                return max(left + grid[x][y], right + grid[x][y], top + grid[x][y], down + grid[x][y])

        for x in range(a):
            for y in range(b):
                if grid[x][y] > 0:
                    gold = max(gold, maxgoldpath(x, y, visited))
        return gold
