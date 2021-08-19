def clonewars(kata_per_day):
    x = max(1, 2 ** (kata_per_day - 1))
    y = 0
    for i in range(0, kata_per_day):
        y += (kata_per_day - i) * 2 ** i
    return [x, y]
