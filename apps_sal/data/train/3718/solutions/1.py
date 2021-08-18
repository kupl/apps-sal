
def divisors5(n):
    return len(list([e for e in [x if n % x == 0 else None for x in range(1, n + 1)] if isinstance(e, int)]))


def divisors4(n):
    return len(list([e for e in [True if n % x == 0 else False for x in range(1, n + 1)] if e]))


def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


def divisors(n): return sum([n % x == 0 for x in range(1, n + 1)])
