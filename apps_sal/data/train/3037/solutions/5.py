from collections import Counter
from functools import lru_cache
from itertools import chain


@lru_cache(maxsize=None)
def func(n):
    return [n] if n & 1 else 2 * func(n >> 1)


def obtain_max_number(arr):
    return max(k * (1 << (v.bit_length() - 1)) for k, v in Counter(chain.from_iterable(map(func, arr))).items())
