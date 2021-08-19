from itertools import accumulate


def polydivisible(x):
    return all((int(''.join(s)) % i == 0 for (i, s) in enumerate(accumulate(str(x)), 1)))
