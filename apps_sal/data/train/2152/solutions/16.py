import itertools as it
import os
import sys


def calc_cost(cumsum, f):
    return sum([min(x % f, f - x % f) for x in cumsum])


def prime_factors(x):
    if not x & 1:
        yield 2
        while not x & 1:
            x >>= 1
    i = 3
    while i * i <= x:
        if x % i == 0:
            yield i
            while x % i == 0:
                x //= i
        i += 2
    if x != 1:
        yield x


def f(xs):
    cumsum = list(it.accumulate(xs))
    s = cumsum[-1]
    if s == 1:
        return -1
    return min((calc_cost(cumsum, f) for f in prime_factors(s)))


def pp(input):
    input()
    xs = list(map(int, input().split()))
    print(f(xs))


if 'paalto' in os.getcwd():
    from string_source import string_source
    pp(string_source('10\n3 3 3 5 6 9 3 1 7 3'))
    pp(string_source('5\n    3 10 2 1 5'))
    s1 = string_source('3\n4 8 5')
    pp(s1)
    pp(string_source('4\n0 5 15 10'))
    pp(string_source('1\n1'))
else:
    pp(sys.stdin.readline)
