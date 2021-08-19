from math import gcd
from functools import reduce


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


try:
    for testcase in range(int(input())):
        d = int(input())
        (f, s, t) = list(map(int, input().split()))
        a = lcm([f, s, t])
        c = 24 * d // a
        print(c)
except:
    EOFError
