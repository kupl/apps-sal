import math
from collections import Counter
from functools import reduce


def proc_arr(arr):  # , k):
    arrstr = "".join(sorted(arr, key=int))
    dupes = reduce((lambda x, y: x * y), [math.factorial(x[1]) for x in Counter(arr).most_common() if x[1] > 1] or [1])
    return [math.factorial(len(arr)) / dupes, int(arrstr), int(arrstr[::-1])]
