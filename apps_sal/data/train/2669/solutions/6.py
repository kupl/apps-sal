from itertools import accumulate, repeat
from functools import reduce
from operator import mul


def value(n):
    return n + reduce(mul, filter(None, map(int, str(n))))


serie = lambda *args: accumulate(repeat(*args), lambda x, _: value(x))
base = set(serie(1, 1000))


def convergence(n):
    return next((i for (i, x) in enumerate(serie(n)) if x in base))
