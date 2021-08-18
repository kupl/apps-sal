
from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
from bisect import bisect_left, bisect_right

mod = 1000000007


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return map(int, stdin.readline().split())


def I():
    return int(stdin.readline())


def printIn(ob):
    return stdout.write(str(ob) + '\n')


def powerLL(n, p):
    result = 1
    while (p):
        if (p & 1):
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result


def myCode():
    n, k = In()
    seq = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            seq.append(-i)
        else:
            seq.append(i)
    if k == math.ceil(n / 2):
        print(*seq)
    elif k < math.ceil(n / 2):
        req = abs(k - (math.ceil(n / 2)))
        for i in range(n - 1, -1, -1):
            if seq[i] > 0:
                seq[i] = -1 * seq[i]
                req -= 1
            if req == 0:
                break
        print(*seq)
    else:
        req = abs(k - (math.ceil(n / 2)))
        for i in range(n - 1, -1, -1):
            if seq[i] < 0:
                seq[i] = -1 * seq[i]
                req -= 1
            if req == 0:
                break
        print(*seq)


def main():
    for t in range(I()):
        myCode()


def __starting_point():
    main()


__starting_point()
