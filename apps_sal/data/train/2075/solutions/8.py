import copy
import itertools
import string
import sys


def powmod(x, p, m):
    if p <= 0:
        return 1
    if p <= 1:
        return x % m
    return powmod(x * x % m, p // 2, m) * (x % m) ** (p % 2) % m


def to_basex(num, x):
    while num > 0:
        yield (num % x)
        num //= x


def from_basex(it, x):
    ret = 0
    p = 1
    for d in it:
        ret += d * p
        p *= x
    return ret


def core():
    _ = input()
    a = [int(x) for x in input().split()]
    r = [int(x) for x in input().split()]
    a.sort()
    r.sort()
    while len(a) > 0 and len(r) > 0 and (r[-1] >= a[-1]):
        a.pop()
        r.pop()
    ans = 'YES' if len(a) > 0 else 'NO'
    print(ans)


core()
