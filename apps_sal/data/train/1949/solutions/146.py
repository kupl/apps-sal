class Solution:
    def dfs(self, pos, sum):
        if pos in self.visit or pos[0] < 0 or pos[0] >= self.M or pos[
                1] < 0 or pos[1] >= self.N or not self.grid[pos[0]][pos[1]]:
            return
        self.visit.add(pos)
        sum += self.grid[pos[0]][pos[1]]
        x, y = pos
        self.maxGold = max(self.maxGold, sum)
        [
            self.dfs(node, sum)
            for node in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        ]
        self.visit.remove(pos)

    def getMaximumGold(self, grid: List[List[int]]):  # -> int:
        self.maxGold = 0
        self.M = len(grid)
        self.N = len(grid[0])
        self.grid = grid
        for beginX in range(self.M):
            for beginY in range(self.N):
                if grid[beginX][beginY] > 0:
                    self.visit = set()
                    self.dfs((beginX, beginY), 0)
        return self.maxGold
