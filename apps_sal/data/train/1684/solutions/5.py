from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
from bisect import bisect_left
mod = 1000000007


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return map(int, stdin.readline().split())


def I():
    return int(stdin.readline())


def printIn(ob):
    return stdout.write(str(ob))


def powerLL(n, p):
    result = 1
    while p:
        if p & 1:
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result


def myCode():
    n = I()
    for i in range(1, n + 1):
        print(i, end=' ')
    print('')


def main():
    for t in range(I()):
        myCode()


def __starting_point():
    main()


__starting_point()
