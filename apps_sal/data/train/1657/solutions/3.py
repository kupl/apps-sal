from itertools import chain, islice
from functools import lru_cache

def reversal_func(s):
    return ''.join(islice(chain.from_iterable(zip(s[::-1], s)), len(s)))

@lru_cache()
def period(n):
    # see https://oeis.org/A216066 , comment by [Robert Pfister, Sep 12 2013]
    # and https://oeis.org/A003558 , formula by [Jonathan Skowera, Jun 29 2013]
    last = 1
    for i in range(n):
        val = abs(2 * n + 1 - 2 * last)
        if val == 1:
            return i + 1
        last = val

def string_func(s,x):
    x %= period(len(s))
    for __ in range(x):
        s = reversal_func(s)
    return s
