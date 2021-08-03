import itertools


def next_pal(val):
    for n in itertools.count(val + 1):
        s = str(n)
        if s == s[::-1]:
            return n
