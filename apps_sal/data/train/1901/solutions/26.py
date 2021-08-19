class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col, index):
            if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])) or (grid[row][col] != 1):
                return 0
            grid[row][col] = index
            area = 1
            for direction in directions:
                area += dfs(row + direction[0], col + direction[1], index)
            return area
        max_area = 0
        found_zero = False
        visited = set()
        index = 2
        area = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area[index] = dfs(row, col, index)
                    index += 1
        max_area = max(area.values() or [0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    indexes = set()
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (grid[new_row][new_col] > 1):
                            indexes.add(grid[new_row][new_col])
                        max_area = max(max_area, sum((area[index] for index in indexes)) + 1)
        return max_area
