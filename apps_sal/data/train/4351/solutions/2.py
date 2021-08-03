from functools import reduce
from operator import mul


def find_middle(string):
    try:
        s = str(reduce(mul, map(int, filter(str.isdigit, string))))
        q, r = divmod(len(s), 2)
        return int(s[q + r - 1:q + 1])
    except TypeError:
        return -1
