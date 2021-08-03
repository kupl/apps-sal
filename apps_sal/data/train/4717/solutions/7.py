def mkP(y): return str(y % 10)
def row(n, x): return " " * (n - x - 1) + "".join(map(mkP, range(1, x + 1))) + "".join(map(mkP, range(x + 1, 0, -1))) + " " * (n - x - 1)


def pattern(n):
    pyramid = [row(n, x) for x in range(n - 1)]
    return '\n'.join(pyramid + [row(n, n - 1)] + list(reversed(pyramid)))
