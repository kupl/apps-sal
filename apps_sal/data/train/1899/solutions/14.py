class Solution:

    def find_island(self, i, j):
        if (i >= 0 and i < self.m) and (j >= 0 and j < self.n) and (self.grid[i][j] == 1):
            self.island.append([i, j])
            self.grid[i][j] = -1
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                self.find_island(i + d[0], j + d[1])

    def expand_island(self):
        while len(self.island) > 0:
            [i, j] = self.island.pop(0)
            for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if i + d[0] in range(self.m) and j + d[1] in range(self.n):
                    if self.grid[i + d[0]][j + d[1]] == 1:
                        return self.grid[i][j] + 1
                    if self.grid[i + d[0]][j + d[1]] == 0:
                        self.island.append([i + d[0], j + d[1]])
                        self.grid[i + d[0]][j + d[1]] = self.grid[i][j] - 1
        return self.m + self.n - 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.grid = A
        (self.m, self.n) = (len(A), len(A[0]))
        self.island = []
        for i in range(self.n):
            for j in range(self.m):
                if len(self.island) == 0 and self.grid[i][j] == 1:
                    self.find_island(i, j)
                    return abs(self.expand_island())
