def find_winner(grid):
    for x in range(4):
        for y in range(4):
            if grid[x][y][0] and len({grid[x][y][i] for i in range(4)}) == 1:
                return grid[x][y][0]
            if grid[0][x][y] and len({grid[i][x][y] for i in range(4)}) == 1:
                return grid[0][x][y]
            if grid[x][0][y] and len({grid[x][i][y] for i in range(4)}) == 1:
                return grid[x][0][y]
            if x == 0 and grid[0][y][0] and (len({grid[i][y][i] for i in range(4)}) == 1):
                return grid[0][y][0]
            if x == 3 and grid[3][y][0] and (len({grid[3 - i][y][i] for i in range(4)}) == 1):
                return grid[3][y][0]
            if y == 0 and grid[x][0][0] and (len({grid[x][i][i] for i in range(4)}) == 1):
                return grid[x][0][0]
            if y == 3 and grid[x][3][0] and (len({grid[x][3 - i][i] for i in range(4)}) == 1):
                return grid[x][3][0]
    for z in range(4):
        if grid[0][0][z] and len({grid[i][i][z] for i in range(4)}) == 1:
            return grid[0][0][z]
        if grid[3][0][z] and len({grid[3 - i][i][z] for i in range(4)}) == 1:
            return grid[3][0][z]
    if grid[0][0][0] and len({grid[i][i][i] for i in range(4)}) == 1:
        return grid[0][0][0]
    if grid[0][3][0] and len({grid[i][3 - i][i] for i in range(4)}) == 1:
        return grid[0][3][0]
    if grid[0][0][3] and len({grid[i][i][3 - i] for i in range(4)}) == 1:
        return grid[0][0][3]
    if grid[0][3][3] and len({grid[i][3 - i][3 - i] for i in range(4)}) == 1:
        return grid[0][3][3]


def play_OX_3D(moves):
    grid = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]
    players = ['O', 'X']
    for (i, (x, y, z)) in enumerate(moves):
        player = players[i % len(players)]
        grid[x][y][z] = player
        winner = find_winner(grid)
        if winner:
            return f'{player} wins after {i + 1} moves'
    return 'No winner'
