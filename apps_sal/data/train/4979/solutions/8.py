rat_dirs = {
    '←': (-1, 0),
    '↑': (0, -1),
    '→': (1, 0),
    '↓': (0, 1),
    '↖': (-1, -1),
    '↗': (1, -1),
    '↘': (1, 1),
    '↙': (-1, 1)
}


def find_piper(town_square, width, height):
    for y in range(height):
        for x in range(width):
            if town_square[y][x] == 'P':
                return x, y
    return -1, -1


def is_rat_deaf(rx, ry, px, py, c):
    dx, dy = px - rx, py - ry
    cx, cy = rat_dirs[c]
    return cx * dx + cy * dy <= 0


def count_deaf_rats(town_square):
    width, height = len(town_square[0]), len(town_square)
    px, py = find_piper(town_square, width, height)
    num_deaf = 0

    for y in range(height):
        for x in range(width):
            c = town_square[y][x]
            if c in rat_dirs and is_rat_deaf(x, y, px, py, c):
                num_deaf += 1

    return num_deaf
