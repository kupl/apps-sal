# No need to store more than the last value so no functools.lru_cache
def ST(n): return 6**n + 5**n - 2**n - 1
def SF(x, y): return (x - 5 * y - 4) // 4


result = []


def gen():
    previous, n = ST(0), 1
    while True:
        current = ST(n)
        val = SF(current, previous)
        if not val % 10:
            yield val
        previous, n = current, n + 1


values = gen()


def find_mult10_SF(n):
    while len(result) < n:
        result.append(next(values))
    return result[n - 1]
