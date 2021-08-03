def peak_height(mountain):
    lX, lY = len(mountain), len(mountain[0])
    top, lst = 0, [[0] * lY for _ in range(lX)]

    for x, row in enumerate(mountain):
        for y, v in enumerate(row):
            lst[x][y] = (v == '^') + (0 < x < lX - 1 and 0 < y < lY - 1 and v == '^' and min(lst[x - 1][y], lst[x][y - 1]))
            top |= lst[x][y] > 0

    for x in reversed(range(1, lX - 1)):
        for y in reversed(range(1, lY - 1)):
            lst[x][y] = min(lst[x][y], lst[x + 1][y] + 1, lst[x][y + 1] + 1)
            top += top < lst[x][y]

    return top
