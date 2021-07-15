D = {
    '↖': -1 -1j, '↑': -1, '↗': -1 +1j,
    '←':    -1j,          '→':    +1j,
    '↙': +1 -1j, '↓': +1, '↘': +1 +1j,
}
def count_deaf_rats(town_square):
    coords = [(i + j * 1j, x) for i, row in enumerate(town_square) for j, x in enumerate(row)]
    p = next(c for c, x in coords if x == 'P')
    return sum(abs(c+D.get(x, 0)-p) > abs(c-p) for c, x in coords)
