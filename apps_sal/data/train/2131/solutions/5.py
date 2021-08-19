from fractions import Fraction
from copy import copy
from random import randint
from collections import *
import sys
sys.setrecursionlimit(1500)


class F:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.save = {}

    def __call__(self, a):
        if a in self.save:
            return self.save[a]
        if type(a) != Fraction:
            a = Fraction(a)
        m = self.m
        n = self.n
        if a == 0:
            return Fraction(-0.5)
        if a == 1:
            return Fraction(-1)
        self.save[a] = 2 * f(a - 1) - (a - 2) * f(1) - 1
        return self.save[a]


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        (g, y, x) = egcd(b % a, a)
        return (g, x - b // a * y, y)


def modinv(a, m):
    (g, x, y) = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


n = int(input())
arr = [int(x) for x in input().split()]
a = []
cnt = defaultdict(int)
for x in arr:
    cnt[x] += 1
for key in cnt:
    cnt[-1] -= 1
cnt[-1] += 1
for (key, value) in list(cnt.items()):
    if key == -1:
        for i in range(value):
            a.append(1)
    else:
        a.append(value + 1)
n = len(a)
m = sum(a)
f = F(m, n)
ans = sum((f(x) for x in a)) - f(m)
MOD = 10 ** 9 + 7
print(ans.numerator * modinv(ans.denominator, MOD) % MOD)
