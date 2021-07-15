from collections import defaultdict


def prime(x):
    for i in xrange(2, x):
        if x % i == 0:
            return False
    return True


def prime_dividers(a):
    return (x for x in xrange(2, abs(a) + 1) if a % x == 0 and prime(x))


def sum_for_list(lst):
    d = defaultdict(int)
    for a in lst:
        for div in prime_dividers(a):
            d[div] += a
    return sorted([list(item) for item in d.iteritems()])
