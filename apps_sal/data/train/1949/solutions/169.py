class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        nrow, ncol = len(grid), len(grid[0])
        possible_starts = [(i, j) for i in range(nrow) for j in range(ncol) if grid[i][j] != 0]

        max_gold = 0
        for start in possible_starts:
            path_stack = [start]
            cell_to_other_paths = collections.defaultdict(list)
            x, y = start
            cumulated_gold = grid[x][y]
            while path_stack:
                found_next = False
                if x - 1 >= 0 and grid[x - 1][y] != 0 and (x - 1, y) not in path_stack:
                    found_next = True
                    tmp_x, tmp_y = x - 1, y
                if x + 1 < nrow and grid[x + 1][y] != 0 and (x + 1, y) not in path_stack:
                    if found_next:
                        cell_to_other_paths[(x, y)].append((x + 1, y))
                    else:
                        found_next = True
                        tmp_x, tmp_y = x + 1, y
                if y - 1 >= 0 and grid[x][y - 1] != 0 and (x, y - 1) not in path_stack:
                    if found_next:
                        cell_to_other_paths[(x, y)].append((x, y - 1))
                    else:
                        found_next = True
                        tmp_x, tmp_y = x, y - 1
                if y + 1 < ncol and grid[x][y + 1] != 0 and (x, y + 1) not in path_stack:
                    if found_next:
                        cell_to_other_paths[(x, y)].append((x, y + 1))
                    else:
                        found_next = True
                        tmp_x, tmp_y = x, y + 1

                if found_next:
                    path_stack.append((tmp_x, tmp_y))
                    cumulated_gold += grid[tmp_x][tmp_y]
                    x, y = tmp_x, tmp_y
                else:
                    max_gold = max(max_gold, cumulated_gold)
                    while path_stack and len(cell_to_other_paths.get(path_stack[-1], [])) == 0:
                        pop_x, pop_y = path_stack.pop(-1)
                        cumulated_gold -= grid[pop_x][pop_y]
                    if not path_stack:
                        break
                    x, y = cell_to_other_paths[path_stack[-1]].pop(0)
                    path_stack.append((x, y))
                    cumulated_gold += grid[x][y]

        return max_gold
