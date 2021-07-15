from itertools import combinations, chain, count
from functools import lru_cache

def segmentations(a):
    def split_at(js):
        i = 0
        for j in js:
            yield a[i:j]
            i = j
        yield a[i:]

    r = range(1, len(a))
    for k in r:
        for sep in combinations(r, k):
            yield split_at(sep)

@lru_cache(maxsize=None)
def value(x, k):
    return sum(int(''.join(L)) for L in chain.from_iterable(segmentations(str(x * k))))

def next_higher(start_value, k):
    return next(x for x in count(start_value+1) if x == value(x, k))
