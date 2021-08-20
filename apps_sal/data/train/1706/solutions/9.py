def rectangle_rotation(a, b):
    (x, y) = (int(a / 2 ** 0.5), int(b / 2 ** 0.5))
    return 2 * x * y + x + y + (x & 1 == y & 1)
