import sys
import math
import os
from io import BytesIO, IOBase
from collections import defaultdict as dd, deque, Counter


def data():
    return sys.stdin.readline().strip()


def mdata():
    return list(map(int, data().split()))


def outl(var):
    sys.stdout.write(' '.join(map(str, var)) + '\n')


def out(var):
    sys.stdout.write(str(var) + '\n')


sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1000000000.0) + 7


def main():
    for t in range(int(data())):
        (a, b) = mdata()
        print(max(a, b, 2 * min(a, b)) ** 2)


def __starting_point():
    main()


__starting_point()
