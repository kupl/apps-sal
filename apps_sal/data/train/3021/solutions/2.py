board = {f'{c}{n}' for c in 'ABCDEFGH' for n in '12345678'}


def available_moves(position):
    if not isinstance(position, str) or position not in board:
        return []
    ((x, y),) = ((ord(c) - 65, int(n) - 1) for (c, n) in (position,))

    def moves(n):
        return ((x, n), (n, y), (x - n, y - n), (x + n, y - n), (x - n, y + n), (x + n, y + n))
    result = {f'{chr(i + 65)}{j + 1}' for n in range(8) for (i, j) in moves(n)}
    return sorted(board & result - {position})
