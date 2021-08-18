from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
import bisect
import heapq as hq


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return list(map(int, stdin.readline().split()))


def I():
    return int(stdin.readline())


P = 1000000007


def main():
    try:
        for _ in range(I()):
            l = L()
            l.sort()
            if (l[0] + l[1] >= l[2]):
                print('Yes')
            else:
                print('No')

    except:
        pass


def __starting_point():
    main()


__starting_point()
