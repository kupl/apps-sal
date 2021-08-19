class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        (rows, cols) = (len(grid), len(grid[0]))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        (start_cell, end_cell) = (None, None)
        empty_cells = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in [0, 1]:
                    empty_cells[i, j] = set()
                    if grid[i][j] == 1:
                        start_cell = (i, j)
                elif grid[i][j] == 2:
                    end_cell = (i, j)
        for (x, y) in empty_cells:
            for (xch, ych) in directions:
                neighbor = (x + xch, y + ych)
                if neighbor in empty_cells:
                    empty_cells[x, y].add(neighbor)
        next_to_finish = set(((end_cell[0] + xch, end_cell[1] + ych) for (xch, ych) in directions))
        visited = set([start_cell])

        def count_routes(cell=start_cell):
            left_to_visit = len(empty_cells) - len(visited)
            if not left_to_visit:
                return int(cell in next_to_finish)
            routes_to_end = 0
            for neighbor in empty_cells[cell] - visited:
                visited.add(neighbor)
                routes_to_end += count_routes(neighbor)
                visited.remove(neighbor)
            return routes_to_end
        return count_routes()
