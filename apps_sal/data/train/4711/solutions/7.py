from math import log, floor


def zeros(n):
    if n < 5:
        return 0
    powers = range(1, floor(log(n, 5)) + 1)
    return sum(n // div for div in (5**pw for pw in powers))
