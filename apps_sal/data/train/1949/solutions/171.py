class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        max_total = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    continue
                start_pos = (i, j)
                visited = {(i, j)}

                stack = [(start_pos, visited, grid[i][j])]
                while stack:
                    (x, y), visited, running_total = stack.pop(0)
                    neighbors = ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))
                    valid_neighbors = [(i, j) for i, j in neighbors if 0 <= i < num_rows and 0 <= j < num_cols and grid[i][j] != 0 and (i, j) not in visited]
                    if not valid_neighbors:
                        if running_total > max_total:
                            max_total = running_total
                        continue
                    else:
                        for x, y in valid_neighbors:
                            copy = visited.copy()
                            copy.add((x, y))
                            stack.append(((x, y), copy, running_total + grid[x][y]))
        return max_total
