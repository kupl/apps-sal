from collections import Counter
import re


def fib(x):
    (a, b) = (0, 1)
    for _ in range(x - 1):
        (a, b) = (b, a + b)
    return b


def around_fib(n):
    fo = fib(n)
    g = Counter(sorted(str(fo)))
    (dig, c) = g.most_common(1)[0]
    return 'Last chunk {}; Max is {} for digit {}'.format(re.findall('\\d{1,25}', str(fo))[-1], c, dig)
