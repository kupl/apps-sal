def shape_area(n):
    return sum([4 * (e - 1) for e in range(n, 1, -1)]) + 1
