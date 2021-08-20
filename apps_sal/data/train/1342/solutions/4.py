from sys import stdin, stdout
import math
from itertools import permutations, combinations, permutations
from collections import defaultdict
from collections import Counter
from bisect import bisect_left
import sys
from queue import PriorityQueue
import operator as op
from functools import reduce
mod = 1000000007


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return list(map(int, stdin.readline().split()))


def I():
    return int(stdin.readline())


def printIn(ob):
    return stdout.write(str(ob) + '\n')


def powerLL(n, p):
    result = 1
    while p:
        if p & 1:
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, list(range(n, n - r, -1)), 1)
    denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom


def myCode():
    (n, x) = In()
    lst = L()
    count = 0
    lst.sort()
    for i in lst:
        if x >= i:
            count += 1
            x = max(x, 2 * i)
        else:
            while x < i:
                count += 1
                x = 2 * x
            count += 1
            x = 2 * i
    print(count)


def main():
    for t in range(I()):
        myCode()


def __starting_point():
    main()


__starting_point()
