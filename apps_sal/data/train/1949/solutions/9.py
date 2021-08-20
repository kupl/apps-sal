class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(row, col, visited, acc=0):
            if (row, col) in visited:
                return 0
            if row < 0 or col < 0 or row >= len(grid) or (col >= len(grid[row])):
                return 0
            if grid[row][col] == 0:
                return 0
            acc += grid[row][col]
            visited.add((row, col))
            ret = max(acc, dfs(row + 1, col, visited, acc), dfs(row - 1, col, visited, acc), dfs(row, col + 1, visited, acc), dfs(row, col - 1, visited, acc))
            visited.remove((row, col))
            return ret
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                ret = max(ret, dfs(row, col, set()))
        return ret
