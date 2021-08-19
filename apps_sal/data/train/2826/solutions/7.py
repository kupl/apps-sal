def r(i):
    return -~i * [1]


def pyramid(n):
    return [*map(r, range(n))]
