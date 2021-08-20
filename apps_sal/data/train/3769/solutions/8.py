import re


def update_grid(px, py, grid):
    height = len(grid)
    width = len(grid[0])
    if px < 0:
        px += 1
        for y in range(height):
            grid[y] = ' ' + grid[y]
    if px >= width:
        for y in range(height):
            grid[y] = grid[y] + ' '
    if py < 0:
        py += 1
        grid.insert(0, ' ' * width)
    if py >= height:
        grid.append(' ' * width)
    grid[py] = grid[py][:px] + '*' + grid[py][px + 1:]
    return (px, py, grid)


def execute(code):
    grid = ['*']
    (x, y) = (0, 0)
    facing = (1, 0)
    while code:
        match = re.match('([FLR])(\\d*)', code)
        code = re.sub('^([FLR])(\\d*)', '', code)
        op = match[1]
        rep = int(match[2] or '1')
        for i in range(rep):
            if op == 'F':
                x += facing[0]
                y += facing[1]
                (x, y, grid) = update_grid(x, y, grid)
            if op == 'L':
                facing = (facing[1], -facing[0])
            if op == 'R':
                facing = (-facing[1], facing[0])
    return '\r\n'.join(grid)
