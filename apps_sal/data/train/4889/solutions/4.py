from itertools import cycle


def max_hexagon_beam(n: int, seq: tuple):
    l = n * 2 - 1  # the number of rows of the hexagon
    ll = [l - abs(n - i - 1) for i in range(l)]  # the lengths of each row
    c = cycle(seq)
    hex = [[next(c) for i in range(j)] for j in ll]    # the hexagon
    sums = [sum(i)for i in hex]  # the straight lines
    for index, i in enumerate(ll):
        start_row = [0, index % n + 1][index >= n]
        hex_row = []
        hex_row2 = []
        for j in range(i):
            y = j + start_row  # the y-axis or the row used
            x = index - [0, y % n + 1][y >= n]  # the x-axis or the position in the row.
            hex_row.append(hex[y][x])  # the line going right-up
            hex_row2.append(hex[y][-1 - x])  # the line going right-down
        sums += [sum(hex_row), sum(hex_row2)]
    sums.sort()
    return sums[-1]

# I also considered extending the hexagon with edges of zeros so the x and y would have less possibility to go out of the list.
