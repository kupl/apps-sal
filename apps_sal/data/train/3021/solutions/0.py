from itertools import product
BOARD = set(map(''.join, product('ABCDEFGH', '12345678')))


def available_moves(position):
    if isinstance(position, str) and position in BOARD:
        return sorted((p for p in BOARD - {position} if abs(ord(p[0]) - ord(position[0])) == abs(int(p[1]) - int(position[1])) or position[0] == p[0] or p[1] == position[1]))
    return []
