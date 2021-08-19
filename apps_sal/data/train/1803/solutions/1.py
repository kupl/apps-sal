from collections import Counter
from itertools import combinations
from functools import reduce
from operator import mul


def best_pal(array):
    (outside, inside) = ([], '')
    for (k, v) in Counter(array).items():
        if v > 1:
            outside.append(k * (v // 2))
        if v % 2:
            inside = max(inside, k)
    outside = ''.join(sorted(outside))
    if outside and outside[-1] == '0':
        outside = ''
    return int(''.join(outside[::-1] + inside + outside))


def numeric_palindrome(*args):
    args = list(filter(None, args))
    if len(args) < 2:
        return 0
    if 1 in args:
        args = list(filter(lambda x: x > 1, args)) + [1]
    if len(args) == 1:
        return best_pal(str(args[0]))
    return max((best_pal(str(reduce(mul, test))) for i in range(2, len(args) + 1) for test in combinations(args, i)))
