# cook your dish here
# Let's hack this code.

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
    while (p):
        if (p & 1):
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result

# --------------------------------------


def myCode():
    n, k, x = In()
    res = []
    j = 0
    if k == 1:
        res = [x for i in range(n)]
    else:
        while j < n:
            i = 0
            while j < n and i < k:
                if i == k - 1:
                    res.append(x)
                else:
                    res.append(0)
                i += 1
                j += 1
    for i in range(n):
        print(res[i], end=' ')
    print("")


def main():
    for t in range(I()):
        myCode()


def __starting_point():
    main()


__starting_point()
