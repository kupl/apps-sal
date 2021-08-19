def ant(grid, col, row, n, direction=0):
    for count in range(n):
        if grid[row][col] == 1:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        grid[row][col] = int(not grid[row][col])
        if direction == 0:
            row -= 1
            if row < 0:
                row = 0
                grid.insert(0, [0 for i in range(len(grid[0]))])
        elif direction == 1:
            col += 1
            if col >= len(grid[0]):
                grid = [row + [0] for row in grid]
        elif direction == 2:
            row += 1
            if row >= len(grid):
                grid.append([0 for i in range(len(grid[0]))])
        else:
            col -= 1
            if col < 0:
                col = 0
                grid = [[0] + row for row in grid]
    return grid
