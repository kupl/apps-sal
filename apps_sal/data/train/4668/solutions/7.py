from functools import reduce


def is_divisible_by_6(s):
    digits = list(range(0, 10))
    perm = [s.replace('*', str(d)) for d in digits]
    res = [s for s in perm if isDiv2(s) and isDiv3(s)]
    return [x.lstrip('0') if len(x) > 1 else x for x in res]


def isDiv2(n):
    return int(n[-1]) % 2 == 0


def isDiv3(n):
    d = [int(x) for x in list(n) if x != '*']
    sum = reduce(lambda a, b: a + b, d)
    return sum % 3 == 0
