'''
We do dfs backtracking starting on each element and try backtrack on every direction by removing from visited set. 

Another good DFS backtracking practice

Time(exponential, around 3^n)
Space(Number of plots with gold)
'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N = len(grid)
        M = len(grid[0])

        def dfs(src, seen, pSum):
            curI, curJ = src[0], src[1]
            if (curI, curJ) not in seen and curI >= 0 and curI < N and curJ >= 0 and curJ < M and grid[curI][curJ] != 0:
                seen.add((curI, curJ))
                pSum += grid[curI][curJ]
                self.sol = max(self.sol, pSum)
                for d in direction:
                    nI, nJ = curI + d[0], curJ + d[1]
                    dfs((nI, nJ), seen, pSum)
                seen.remove((curI, curJ))
        self.sol = -1
        for i in range(N):
            for j in range(M):
                if grid[i][j] != 0:
                    seen = set()
                    dfs((i, j), seen, 0)
        return self.sol
