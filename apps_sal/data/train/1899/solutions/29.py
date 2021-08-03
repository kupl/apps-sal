class Solution:

    def find_island(self, i, j):
        self.island.append([i, j])
        self.grid[i][j] = -1
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for d in D:
            if (i + d[0] in range(self.m)) and (j + d[1] in range(self.n)) and (self.grid[i + d[0]][j + d[1]] == 1):
                self.find_island(i + d[0], j + d[1])

    def expand_island(self):
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(self.island) > 0:
            [i, j] = self.island.pop(0)
            depth = abs(self.grid[i][j])
            for d in D:
                if (i + d[0] in range(self.m)) and (j + d[1] in range(self.n)):
                    if self.grid[i + d[0]][j + d[1]] == 1:
                        return depth - 1
                    if self.grid[i + d[0]][j + d[1]] == 0:
                        self.island.append([i + d[0], j + d[1]])
                        self.grid[i + d[0]][j + d[1]] = -1 * (depth + 1)

        return self.m + self.n - 1

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.grid = A
        self.m = len(A)
        self.n = len(A[0])
        self.island = []
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and len(self.island) == 0:
                    self.find_island(i, j)

        res = self.expand_island()

        return res
