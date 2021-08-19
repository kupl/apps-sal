class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid.insert(0, [0 for i in range(len(grid[0]))])
        grid.append([0 for i in range(len(grid[0]))])
        islands = []
        max_length = 1
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] != 1:
                    continue
                island_id = len(islands)
                length = 0
                connect_length = 0
                queue = [(i, j)]
                grid[i][j] = 2 + island_id
                while queue:
                    (x, y) = queue.pop()
                    for (dx, dy) in directions:
                        this_grid = grid[x + dx][y + dy]
                        if this_grid == 1:
                            grid[x + dx][y + dy] = 2 + island_id
                            queue.append((x + dx, y + dy))
                        elif isinstance(this_grid, list):
                            new_connect = 0
                            already = False
                            for old_island_id in this_grid:
                                if old_island_id != island_id:
                                    new_connect += islands[old_island_id]
                                else:
                                    already = True
                            if not already:
                                connect_length = max(connect_length, new_connect)
                                this_grid.append(island_id)
                        else:
                            grid[x + dx][y + dy] = [island_id]
                    length += 1
                islands.append(length)
                max_length = max(max_length, length + connect_length + 1)
        return min(max_length, (len(grid) - 2) * (len(grid[0]) - 2))
