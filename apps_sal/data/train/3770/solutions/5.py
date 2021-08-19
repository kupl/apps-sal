def to_1D(x, y, size):
    # x is the index of a column and y the index of a row
    return y * size[0] + x


def to_2D(n, size):
    return (n % size[0], n // size[0])
