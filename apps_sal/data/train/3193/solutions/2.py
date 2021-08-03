from itertools import chain


def gen(x): return chain(range(1, x + 1), range(x, 0, -1))
def concat(x): return ' '.join(str(y % 10) for y in gen(x))
def padding(size): return lambda x: f"{concat(x): >{size}}"


def stairs(n):
    return '\n'.join(map(padding(4 * n - 1), range(1, n + 1)))
