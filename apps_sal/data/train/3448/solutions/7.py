from functools import reduce
def f(n):
    return None if not isinstance(n, int) or n<1 else reduce(lambda x, y: x + y, range(1, n + 1))
