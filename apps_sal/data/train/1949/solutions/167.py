class Solution:

    def is_valid(self, grid, i, j):
        valid_i = 0 <= i <= len(grid) - 1
        valid_j = 0 <= j <= len(grid[0]) - 1
        if not valid_i or not valid_j:
            return False
        if grid[i][j] == 0:
            return False
        return True

    def find_path(self, grid, i, j, gold, visited, max_gold):
        visited.add((i, j))
        gold += grid[i][j]
        max_gold[0] = max(gold, max_gold[0])
        for (x_, y_) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self.is_valid(grid, i + x_, j + y_) and (not (i + x_, j + y_) in visited):
                self.find_path(grid, i + x_, j + y_, gold, visited, max_gold)
        visited.remove((i, j))

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = [float('-inf')]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.find_path(grid, i, j, 0, set(), max_gold)
        return max_gold[0] if max_gold != float('-inf') else 0
