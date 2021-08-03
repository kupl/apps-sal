class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        grid_height, grid_width = len(grid), len(grid[0])
        visited = set()

        def helper(i, j, gold=0):
            if i < 0 or i >= grid_height or j < 0 or j >= grid_width or (i, j) in visited or grid[i][j] == 0:
                return gold
            visited.add((i, j))
            res = 0
            for (a, b) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                res = max(helper(i + a, j + b, gold + grid[i][j]), res)
            visited.remove((i, j))
            return res

        result = 0
        for i in range(grid_height):
            for j in range(grid_width):
                result = max(helper(i, j), result)
        return result
