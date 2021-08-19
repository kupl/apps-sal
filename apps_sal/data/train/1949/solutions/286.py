class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        result = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j, total=0):
            nonlocal result
            result = max(result, total)
            visited.add((i, j))
            for (dx, dy) in directions:
                (rx, cy) = (i + dx, j + dy)
                if 0 <= rx < R and 0 <= cy < C and ((rx, cy) not in visited) and (grid[rx][cy] != 0):
                    dfs(rx, cy, total + grid[rx][cy])
            visited.remove((i, j))
        visited = set()
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    dfs(i, j, grid[i][j])
        return result
