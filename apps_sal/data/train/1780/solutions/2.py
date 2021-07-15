from functools import lru_cache, reduce
from operator import or_
from statistics import mean, median

@lru_cache(maxsize=None)
def prod(n, x):
    if n < 0:
        return set()
    return reduce(or_, ({i*s for s in prod(n-i, i)} for i in range(2, x+1)), {1})

def part(n):
    xs = prod(n, n)
    return f"Range: {max(xs) - min(xs)} Average: {mean(xs):.2f} Median: {median(xs):.2f}"
