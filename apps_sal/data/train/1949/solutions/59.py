class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        visited = []
        visited_in = []
        for i in range(m):
            for j in range(n):
                visited_in.append(False)
            visited.append(visited_in)
            visited_in = []

        def inArea(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def DFS(grid, startx, starty):
            res = 0
            visited[startx][starty] = True
            for i in range(4):
                newx = startx + d[i][0]
                newy = starty + d[i][1]
                if inArea(newx, newy) and (not visited[newx][newy]) and grid[newx][newy] != 0:
                    res = max(res, grid[newx][newy] + DFS(grid, newx, newy))

            visited[startx][starty] = False
            return res

        record_each_result = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (not visited[i][j]):
                    result = grid[i][j] + DFS(grid, i, j)
                    record_each_result.append(result)

        final_result = max(record_each_result)
        return final_result
