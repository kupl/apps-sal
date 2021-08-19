from functools import cmp_to_key


def cmp(a, b):
    return int('%i%i' % (b, a)) - int('%i%i' % (a, b))


def largest_arrangement(n):
    return int(''.join((str(i) for i in sorted(n, key=cmp_to_key(cmp)))))
