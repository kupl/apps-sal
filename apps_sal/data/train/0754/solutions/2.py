import sys
import io
import os
import math
from math import ceil, log, gcd, inf
from itertools import permutations
mod = 1000000007
mod1 = 998244353


def printlist(n):
    sys.stdout.write(' '.join(map(str, n)) + '\n')


def printf(n):
    return sys.stdout.write(str(n) + '\n')


def printns(n):
    sys.stdout.write(str(n))


def intinp():
    return int(sys.stdin.readline())


def strinp():
    return sys.stdin.readline()


def arrinp():
    return list(map(int, sys.stdin.readline().strip().split()))


def mulinp():
    return list(map(int, sys.stdin.readline().strip().split()))


def flush():
    return sys.stdout.flush()


def power_two(x):
    return 1 << x


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    n = str(intinp())
    for i in n:
        if int(i) % 2 == 0:
            print(1)
            return 0
    print(0)


def main():
    tc = intinp()
    while tc:
        solve()
        tc -= 1


main()
