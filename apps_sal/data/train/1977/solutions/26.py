class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        # for row in grid:
        #    print(row)

        def dfs(i, j):
            if i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1:
                return False
            else:
                for vi, vj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    newI = vi + i
                    newJ = vj + j
                    if grid[newI][newJ] == 0:
                        # if self.total == 4:
                        #    print(newI, newJ)
                        grid[newI][newJ] = 1
                        self.curPath.append((newI, newJ))

                        # print('what')
                        if not dfs(newI, newJ):
                            return False

            # for k, h in self.curPath:
            #    grid[k][h] = self.total+2
            return True

        self.total = 0
        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                if grid[i][j] == 0:
                    #print(i, j)
                    grid[i][j] = 1
                    self.curPath = [(i, j)]
                    if dfs(i, j):
                        self.total += 1
                        #print(self.curPath, len(self.curPath), -self.total)
                        for k, h in self.curPath:
                            grid[k][h] = -self.total
                    else:
                        for k, h in self.curPath:
                            grid[k][h] = 0

                        # for row in grid:
                        #    print(row)
        return self.total
