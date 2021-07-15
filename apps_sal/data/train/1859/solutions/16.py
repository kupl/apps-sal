class Solution:
    def memoization(self, grid, i, j, memo):
        if i == len(grid)-1 or j == len(grid[0])-1:
            return int(grid[i][j] == 1)
        if memo[i][j] is None:
            if grid[i][j] == 0:
                memo[i][j] = 0
            else:
                col = self.memoization(grid, i, j+1, memo)
                row = self.memoization(grid, i+1, j, memo)
                diag = self.memoization(grid, i+1, j+1, memo)
                memo[i][j] = min(min(col, row), diag) + 1
        return memo[i][j]
                
    def countSquares(self, matrix: List[List[int]]) -> int:
        memo = [[None for j in range(len(matrix[0]))] for i in range(len(matrix))]
        out = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out += self.memoization(matrix, i, j, memo)
        return out
