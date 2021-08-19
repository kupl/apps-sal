class Solution:
    def getDegree(self, i, j, grid: List[List[int]]) -> int:
        deg = 0
        if i > 0 and grid[i - 1][j] > 0:
            deg += 1
        if i < len(grid) - 1 and grid[i + 1][j] > 0:
            deg += 1
        if j > 0 and grid[i][j - 1] > 0:
            deg += 1
        if j < len(grid[0]) - 1 and grid[i][j + 1] > 0:
            deg += 1
        return deg

    def traverseMaxGoldDfs(self, i, j, grid) -> int:
        # use dfs to get the max gold.
        degree = self.getDegree(i, j, grid)
        if degree == 0:
            return grid[i][j]

        # then, check neighbours
        temp = grid[i][j]
        grid[i][j] = 0
        gold = temp
        res = 0
        if i > 0 and grid[i - 1][j] > 0:
            res = max(res, self.traverseMaxGoldDfs(i - 1, j, grid))
        if i < len(grid) - 1 and grid[i + 1][j] > 0:
            res = max(res, self.traverseMaxGoldDfs(i + 1, j, grid))
        if j > 0 and grid[i][j - 1] > 0:
            res = max(res, self.traverseMaxGoldDfs(i, j - 1, grid))
        if j < len(grid[0]) - 1 and grid[i][j + 1] > 0:
            res = max(res, self.traverseMaxGoldDfs(i, j + 1, grid))

        gold = max(gold, temp + res)
        grid[i][j] = temp
        return gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                degree = self.getDegree(i, j, grid)
                if grid[i][j] > 0 and (degree <= 1 or degree > 2):
                    # traverse using bfs from here.
                    gold = self.traverseMaxGoldDfs(i, j, grid)
                    if gold > maxGold:
                        maxGold = gold
        return maxGold
