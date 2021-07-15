import itertools as it
import os
import sys


def calc_cost(cumsum, f):
    return sum([min(x % f, f - x % f) for x in cumsum])


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)

    return factors


def f(xs):
    cumsum = list(it.accumulate(xs))
    s = cumsum[-1]
    if s == 1:
        return -1

    return min(calc_cost(cumsum, f) for f in prime_factors(s))


def pp(input):
    input()
    xs = list(map(int, input().split()))
    print(f(xs))


if "paalto" in os.getcwd():
    from string_source import string_source

    pp(
        string_source(
            """10
3 3 3 5 6 9 3 1 7 3"""
        )
    )

    pp(
        string_source(
            """5
    3 10 2 1 5"""
        )
    )

    s1 = string_source(
        """3
4 8 5"""
    )
    pp(s1)

    pp(
        string_source(
            """4
0 5 15 10"""
        )
    )

    pp(
        string_source(
            """1
1"""
        )
    )

else:
    pp(sys.stdin.readline)

