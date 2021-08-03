class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.nums = grid.copy()
        self.results = []
        self.visited = [[False for i in range(len(grid[0]))]for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] != 0:
                    maxVal = self.getTheGold(i, j, 0)

        return max(self.results)

    def getTheGold(self, i, j, value):
        # print(i,j)
        if self.isSafe(i, j):
            self.visited[i][j] = True
            self.getTheGold(i + 1, j, value + self.nums[i][j])
            self.getTheGold(i, j + 1, value + self.nums[i][j])
            self.getTheGold(i - 1, j, value + self.nums[i][j])
            self.getTheGold(i, j - 1, value + self.nums[i][j])
            self.visited[i][j] = False

        else:

            return self.results.append(value)

    def isSafe(self, i, j):
        if i >= 0 and i < len(self.nums) and j >= 0 and j < len(self.nums[0]):

            return self.nums[i][j] != 0 and self.visited[i][j] == False

        return False
