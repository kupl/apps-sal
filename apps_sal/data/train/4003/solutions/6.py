moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))


def possible_positions(pos):
    x, y = ord(pos[0]) - 96, int(pos[1])
    return [f"{chr(96 + x + i)}{y + j}" for i, j in moves if -i < x < 9 - i and -j < y < 9 - j]
