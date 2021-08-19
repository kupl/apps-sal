def shape_area(n):
    return 2 * sum((x for x in range(1, 2 * (n - 1), 2))) + (2 * n - 1)
