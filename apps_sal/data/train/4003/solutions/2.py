import string

KNIGHT = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
BOARD_SIZE = 8


def moves(x, y, directions):
    for dx, dy in directions:
        x2, y2 = x + dx, y + dy
        if 0 <= x2 < BOARD_SIZE > y2 >= 0:
            yield x2, y2


def possible_positions(pos):
    x, y = (string.ascii_lowercase.find(pos[0]), int(pos[1]) - 1)
    return [f'{string.ascii_lowercase[x]}{y+1}' for x, y in moves(x, y, KNIGHT)]
