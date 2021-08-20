def to_1D(x, y, size):
    return x + y * size[0]


def to_2D(n, size):
    c = 0
    for i in range(size[1]):
        for j in range(size[0]):
            if n == c:
                return (j, i)
            c += 1
