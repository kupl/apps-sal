class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        touched = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if touched[i][j] or grid[i][j]:
                    continue
                island = True
                to_explore = [[i, j]]
                while to_explore:
                    (c_i, c_j) = to_explore.pop(0)
                    if c_i - 1 < 0:
                        island = False
                    elif not touched[c_i - 1][c_j] and (not grid[c_i - 1][c_j]):
                        to_explore.append([c_i - 1, c_j])
                    if c_i + 1 >= len(grid):
                        island = False
                    elif not touched[c_i + 1][c_j] and (not grid[c_i + 1][c_j]):
                        to_explore.append([c_i + 1, c_j])
                    if c_j - 1 < 0:
                        island = False
                    elif not touched[c_i][c_j - 1] and (not grid[c_i][c_j - 1]):
                        to_explore.append([c_i, c_j - 1])
                    if c_j + 1 >= len(grid[0]):
                        island = False
                    elif not touched[c_i][c_j + 1] and (not grid[c_i][c_j + 1]):
                        to_explore.append([c_i, c_j + 1])
                    touched[c_i][c_j] = 1
                if island:
                    num_islands += 1
        return num_islands
