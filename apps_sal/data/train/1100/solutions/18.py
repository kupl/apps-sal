from sys import stdin, stdout
from math import gcd, ceil, sqrt


def ii1():
    return int(stdin.readline().strip())


def is1():
    return stdin.readline().strip()


def iia():
    return list(map(int, stdin.readline().strip().split()))


def isa():
    return stdin.readline().strip().split()


mod = 1000000007
tc = ii1()
for _ in range(tc):
    (p, q, r) = iia()
    (a, b, c) = iia()
    if a < p or b < q or c < r:
        print(-1)
    else:
        add = [a - p, b - q, c - r]
        print(sum(add))
