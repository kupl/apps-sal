#=============templates==============#
from math import floor, ceil, log2
import sys
def takeArr(): return list(map(int, input().split()))
def takeList(): return list(map(int, input().split()))


sys.setrecursionlimit(10**6)
# import itertools
# import collections
#==================MAIN==================#


def powOfPositive(n):
    pos = floor(log2(n))
    return 2**pos


def powOfNegative(n):
    pos = ceil(log2(n))
    return (-1 * pow(2, pos))


def highestPowerOf2(n):
    if (n > 0):
        return powOfPositive(n)
    else:
        n = -n
        return powOfNegative(n)


def main(t):
    x, y = takeArr()
    a, b = x + 1, y + 1
    sa = sb = 0
    while a:
        a -= highestPowerOf2(a)
        sa += 1
    while b:
        b -= highestPowerOf2(b)
        sb += 1

    winner = 2 if sa > sb else 1 if sb > sa else 0
    score = abs(sa - sb) if winner else 0
    print(winner, score)
    if t > 1:
        main(t - 1)


main(int(input()))

#==================END==================#
