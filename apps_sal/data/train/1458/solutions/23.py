import sys
import math
import bisect
from math import factorial as fact


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def rinput():
    return map(int, sys.stdin.readline().strip().split())


def get_list():
    return list(map(int, sys.stdin.readline().strip().split()))


mod = int(1000000000.0) + 7


def ncr(n, i):
    num = fact(n)
    den = fact(i) * fact(n - i)
    return num // den


for _ in range(iinput()):
    n = iinput()
    ans = 0
    for i in range(1, n + 1, 2):
        ans += (n - i + 1) * (n - i + 1)
    print(ans)
