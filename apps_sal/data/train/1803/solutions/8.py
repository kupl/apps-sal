from functools import reduce
from itertools import combinations
from collections import Counter


def max_palindrome(num):
    counter = Counter(str(num))
    one = [int(x) for (x, v) in list(counter.items()) if v % 2 == 1]
    if 0 < len(one):
        one = str(max(one))
    else:
        one = ''
    more = []
    for x in counter:
        while 2 <= counter[x]:
            more.append(x)
            counter[x] -= 2
    more.sort()
    if 0 < len(more) and more[-1] == '0':
        more = ''
    more = ''.join(more)
    res = more[::-1] + one + more
    return int(res)


def numeric_palindrome(*args):
    palindromes = []
    one = args.count(1)
    args = [arg for arg in args if 1 < arg]
    if 0 < one:
        args.append(1)
    if 1 < one:
        args.append(1)
    for n in range(2, len(args) + 1):
        comb = list(combinations(args, n))
        for c in comb:
            product = reduce(lambda a, b: a * b, c)
            palindromes.append(max_palindrome(product))
    return max(palindromes) if 0 < len(palindromes) else 0
