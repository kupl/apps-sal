board = {f'{c}{n}' for c in 'ABCDEFGH' for n in '12345678'}


def available_moves(position):
    if not isinstance(position, str) or position not in board:
        return []
    ((x, y),) = ((ord(c), ord(n)) for (c, n) in (position,))

    def moves(m):
        return ((x, m + 49), (m + 65, y), (x - m, y - m), (x + m, y - m), (x - m, y + m), (x + m, y + m))
    result = {f'{chr(i)}{chr(j)}' for m in range(8) for (i, j) in moves(m)}
    return sorted(board & result - {position})
