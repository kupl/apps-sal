class Solution:
    def getMaxGoldHelper(self, visited, grid, curx, cury):
        if (curx, cury) in visited:
            return 0
        visited.add((curx, cury))
        ret = grid[cury][curx]
        max_recur = 0
        for (nextx, nexty) in [(curx - 1, cury), (curx + 1, cury), (curx, cury - 1), (curx, cury + 1)]:
            if nextx < 0 or nextx >= len(grid[0]) or nexty < 0 or nexty >= len(grid):
                continue
            if grid[nexty][nextx] > 0:
                max_recur = max(max_recur, self.getMaxGoldHelper(visited, grid, nextx, nexty))
        visited.remove((curx, cury))
        return ret + max_recur

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_seen = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                max_seen = max(max_seen, self.getMaxGoldHelper(set(), grid, col, row))
        return max_seen
