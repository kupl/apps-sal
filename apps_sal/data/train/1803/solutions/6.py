import itertools
from functools import reduce
from operator import mul
import re


def max_palindrome(x):
    s = str(x)
    left, odds = [], []
    for c in set(s):
        cnt = s.count(c)
        d, d1 = cnt//2, cnt % 2
        if d:
            left.append(c*d)
        if d1:
            odds.append(c)
    left.sort(reverse=True)
    s1 = ''.join(left)
    m = max(odds) if odds else ''
    temp = s1+m+s1[::-1]
    temp = re.sub(r'0*$', '', temp)
    return int(temp)


def numeric_palindrome(*args):
    arr = [x for x in args if x > 1]
    if 1 in args:
        arr.append(1)
    if len(arr) > 1:
        res = 0
        for i in range(2, len(arr)+1):
            temp = [max_palindrome(reduce(mul, x))
                    for x in itertools.combinations(arr, i)]
            res = max(max(temp), res)
        return res
    elif len(arr) == 1:
        return max_palindrome(arr[0]) if args.count(1)>1 in args else 0
    else:
        return 1 if args.count(1) > 1 else 0

