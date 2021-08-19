"""
      ___           ___                         ___                       ___           ___                         ___
     /\\__\\         /\\  \\         _____         /\\  \\                     /\\  \\         /\\  \\                       /\\__    /:/ _/_        \\:\\  \\       /::\\  \\        \\:\\  \\       ___         /::\\  \\       |::\\  \\         ___         /:/ _/_
   /:/ /\\  \\        \\:\\  \\     /:/\\:\\  \\        \\:\\  \\     /\\__\\       /:/\\:\\__\\      |:|:\\  \\       /\\__\\       /:/ /\\    /:/ /::\\  \\   ___  \\:\\  \\   /:/  \\:\\__\\   ___ /::\\  \\   /:/__/      /:/ /:/  /    __|:|\\:\\  \\     /:/  /      /:/ /::\\   /:/_/:/\\:\\__\\ /\\  \\  \\:\\__\\ /:/__/ \\:|__| /\\  /:/\\:\\__\\ /::\\  \\     /:/_/:/__/___ /::::|_\\:\\__\\   /:/__/      /:/_/:/\\:\\__ \\:\\/:/ /:/  / \\:\\  \\ /:/  / \\:\\  \\ /:/  / \\:\\/:/  \\/__/ \\/\\:\\  \\__  \\:\\/:::::/  / \\:\\~~\\  \\/__/  /::\\  \\      \\:\\/:/ /:/  /
  \\::/ /:/  /   \\:\\  /:/  /   \\:\\  /:/  /   \\::/__/       ~~\\:\\/\\__\\  \\::/~~/~~~~   \\:\\  \\       /:/\\:\\  \\      \\::/ /:/  /
   \\/_/:/  /     \\:\\/:/  /     \\:\\/:/  /     \\:\\  \\          \\::/  /   \\:\\~~\\        \\:\\  \\      \\/__\\:\\  \\      \\/_/:/  /
     /:/  /       \\::/  /       \\::/  /       \\:\\__\\         /:/  /     \\:\\__\\        \\:\\__\\          \\:\\__\\       /:/  /
     \\/__/         \\/__/         \\/__/         \\/__/         \\/__/       \\/__/         \\/__/           \\/__/       \\/__/

"""
from sys import stdin, stdout, setrecursionlimit
from functools import reduce
from bisect import bisect_right, bisect_left, bisect
from math import gcd, inf, sqrt, pi, cos, sin, ceil, log2, floor, log
from collections import deque
import operator as op
import collections
import math
import sys
'\n░░██▄░░░░░░░░░░░▄██\n░▄▀░█▄░░░░░░░░▄█░░█░\n░█░▄░█▄░░░░░░▄█░▄░█░\n░█░██████████████▄█░\n░█████▀▀████▀▀█████░\n▄█▀█▀░░░████░░░▀▀███\n██░░▀████▀▀████▀░░██\n██░░░░█▀░░░░▀█░░░░██\n███▄░░░░░░░░░░░░▄███\n░▀███▄░░████░░▄███▀░\n░░░▀██▄░▀██▀░▄██▀░░░\n░░░░░░▀██████▀░░░░░░\n░░░░░░░░░░░░░░░░░░░░\n'
setrecursionlimit(2 ** 20)


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(factors)


def isPowerOfTwo(x):
    return x and (not x & x - 1)


MOD = 1000000007
PMOD = 998244353
N = 10 ** 18 + 1
LOGN = 30
alp = 'abcdefghijklmnopqrstuvwxyz'
T = 1
T = int(stdin.readline())
for _ in range(T):
    (n, m) = list(map(int, stdin.readline().rstrip().split()))
    p = n * (n + 1) // 2 - ceil(n / 2) ** 2
    print(pow(m, p, MOD))
