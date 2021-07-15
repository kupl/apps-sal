from functools import reduce
from itertools import count, islice
from operator import mul

def gen(n):
    yield n
    while True:
        n += n if n < 10 else reduce(mul, map(int, str(n).replace('0', '')), 1)
        yield n

def convergence(n, base_series = set(islice(gen(1), 1000))):
    it = gen(n)
    return next(i for i in count() if next(it) in base_series)
