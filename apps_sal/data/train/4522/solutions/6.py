def right(x, y, z):
    x, y, z = sorted([x, y, z])
    return x ** 2 + y ** 2 == z ** 2


def side_len(x, y):
    return [z for z in range(y - x + 1, x + y) if not right(x, y, z)]
