from math import ceil
from itertools import count


def graceful_tipping(bill):
    num = ceil(bill * 0.15 + bill)
    if num < 10:
        return num
    d = int('5' + ((len(str(num)) - 2) * '0'))
    for n in count(num):
        if n % d == 0:
            return n
