columns = 'ABCDEFGH'


def available_moves(position):
    if not (isinstance(position, str) and len(position) == 2):
        return []
    c0, r0 = position
    if not ('A' <= c0 <= 'H' and '1' <= r0 <= '8'):
        return []
    c, r = columns.index(c0), int(r0) - 1
    xs = {(i, r) for i in range(8)}
    xs |= {(c, i) for i in range(8)}
    xs |= {(i, r + c - i) for i in range(8) if 0 <= r + c - i < 8}
    xs |= {(i, r + i - c) for i in range(8) if 0 <= r + i - c < 8}
    xs.remove((c, r))
    return [f'{columns[c]}{r+1}' for c, r in sorted(xs)]
