class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def initVisit(m, n):
            visited = {}
            for i in range(m):
                for j in range(n):
                    visited[i, j] = -1
            return visited
        maxGold = 0

        def check(i, j):
            if 0 <= i < m and 0 <= j < n and (grid[i][j] != 0) and (visited[i, j] != 1):
                return True
            else:
                return False

        def helper(i, j):
            moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            maxSum = 0
            for move in moves:
                (nextI, nextJ) = (move[0] + i, move[1] + j)
                if check(nextI, nextJ):
                    visited[i, j] = 1
                    maxSum = max(maxSum, helper(nextI, nextJ))
                    visited[i, j] = 0
            return maxSum + grid[i][j]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited = initVisit(m, n)
                    visited[i, j] = 1
                    maxGold = max(maxGold, helper(i, j))
        return maxGold
