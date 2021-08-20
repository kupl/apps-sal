from functools import reduce
from operator import mul


def something_acci(n):
    li = [1, 1, 2, 2, 3, 3]
    while True:
        li.append(reduce(mul, li[-3:]) - reduce(mul, li[-6:-3]))
        if len(str(li[-1])) >= n:
            return (len(li), len(str(li[-1])))
