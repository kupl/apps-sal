from itertools import count as c


def find_lowest_int(k):
    return next((n for n in c(1) if sorted(str(n * k)) == sorted(str(n * (k + 1)))))
