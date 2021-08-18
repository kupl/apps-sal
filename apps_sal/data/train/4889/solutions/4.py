from itertools import cycle


def max_hexagon_beam(n: int, seq: tuple):
    l = n * 2 - 1
    ll = [l - abs(n - i - 1) for i in range(l)]
    c = cycle(seq)
    hex = [[next(c) for i in range(j)] for j in ll]
    sums = [sum(i)for i in hex]
    for index, i in enumerate(ll):
        start_row = [0, index % n + 1][index >= n]
        hex_row = []
        hex_row2 = []
        for j in range(i):
            y = j + start_row
            x = index - [0, y % n + 1][y >= n]
            hex_row.append(hex[y][x])
            hex_row2.append(hex[y][-1 - x])
        sums += [sum(hex_row), sum(hex_row2)]
    sums.sort()
    return sums[-1]
