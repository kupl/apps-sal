def to_1D(x, y, size):
    w, h = size
    return x + y * w


def to_2D(n, size):
    w, h = size
    return (n % w, n // w)
