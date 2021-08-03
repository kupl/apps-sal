import sys
import io
import os
import math
from math import ceil, log, gcd, inf
from itertools import permutations
mod = 1000000007
mod1 = 998244353


def printlist(n):
    sys.stdout.write(" ".join(map(str, n)) + "\n")


def printf(n): return sys.stdout.write(str(n) + "\n")


def printns(n):
    sys.stdout.write(str(n))


def intinp():
    return int(sys.stdin.readline())


def strinp():
    return sys.stdin.readline()


def arrinp():
    return list(map(int, sys.stdin.readline().strip().split()))


def mulinp():
    return map(int, sys.stdin.readline().strip().split())


def flush():
    return sys.stdout.flush()


def power_two(x):
    return (1 << x)


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    n, m = mulinp()
    t = set(arrinp())
    t2 = set(arrinp())
    temp = t.difference(t2)
    temp1 = t2.difference(t)
    ans = temp.union(temp1)
    for i in ans:
        print(i, end=" ")
    print()


def main():
    tc = intinp()
    while(tc):
        solve()
        tc -= 1


main()
