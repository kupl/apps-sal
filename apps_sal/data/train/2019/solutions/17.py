import collections
import itertools
import fractions
import functools
import heapq
import math
import queue


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(a) / (n - 1)
    return max(max(a), math.ceil(x))


def __starting_point():
    print(solve())


__starting_point()
