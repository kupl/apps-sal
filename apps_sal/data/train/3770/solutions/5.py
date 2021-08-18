def to_1D(x, y, size):
    return y * size[0] + x


def to_2D(n, size):
    return (n % size[0], n // size[0])
