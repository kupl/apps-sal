class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            if grid[i][0] == 0:
                grid[i][0] = -2
            if grid[i][width - 1] == 0:
                grid[i][width - 1] = -2
        for j in range(width):
            if grid[0][j] == 0:
                grid[0][j] = -2
            if grid[height - 1][j] == 0:
                grid[height - 1][j] = -2
        count = 0
        for i in range(1, height - 1):
            for j in range(1, width - 1):
                flag = 0
                visted_list = []
                if grid[i][j] == 0:
                    visted_list.append([i, j])
                    grid[i][j] = -1
                    while len(visted_list) > 0:
                        current_index = visted_list.pop()
                        ii = current_index[0]
                        jj = current_index[1]
                        indexes = [(ii - 1, jj), (ii + 1, jj), (ii, jj - 1), (ii, jj + 1)]
                        for (a, b) in indexes:
                            if grid[a][b] == 0:
                                visted_list.append([a, b])
                                grid[a][b] = -1
                            if grid[a][b] == -2:
                                flag = 1
                    if flag == 0:
                        count += 1
        return count
