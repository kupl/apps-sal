class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.num_closed_islands = 0
        self.visited = set()
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                if grid[i][j] == 0 and (i, j) not in self.visited:
                    self.include = True
                    self.dfs(i, j)
                    if self.include:
                        self.num_closed_islands += 1
        return self.num_closed_islands

    def dfs(self, i, j):
        if i == 0 or j == 0 or i == (self.m - 1) or j == (self.n - 1):
            self.include = False
        self.visited.add((i, j))
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, next_j = i + x , j + y
            if (self.in_range(next_i, next_j) and 
                (next_i, next_j) not in self.visited and 
                self.grid[next_i][next_j] == 0):
                self.dfs(next_i, next_j)
\t\t
    def in_range(self, i, j):
        return  0 <= i < self.m and 0 <= j < self.n

