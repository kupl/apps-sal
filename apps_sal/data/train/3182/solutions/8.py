from itertools import islice

def iter_powers(n):
    x = n
    while True:
        yield from map(int, str(x))
        x *= n


def LDTA(n):
    appear = set(range(10))
    for x in islice(iter_powers(n), 1000):
        appear.discard(x)
        if len(appear) == 1:
            return appear.pop()
