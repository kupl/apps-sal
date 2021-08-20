from collections import defaultdict
import sys
import math
import random
import bisect
sys.setrecursionlimit(10 ** 6)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


arr = [0]
for i in range(1, 5 * 10 ** 4):
    arr.append(arr[-1] + i)
for _ in range(int(input())):
    n = int(input())
    ind = bisect.bisect_left(arr, n)
    print(min(n - ind + 1, ind * (ind - 1) // 2))
