from itertools import count


def find_lowest_int(k):
    return next(n for n in count(1) if sorted(str(n * k)) == sorted(str(n * (k + 1))))
