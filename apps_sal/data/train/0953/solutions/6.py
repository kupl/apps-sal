from collections import defaultdict
import sys
import math as mt
import random
sys.setrecursionlimit(10 ** 6)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


ans = [0] * (10 ** 6 + 1)
ans[2] = 1
ans[3] = 1
start = 3
for i in range(4, 10 ** 6 + 1):
    ans[i] = min(start * (start - 1) // 2, i - start + 1)
    if ans[i] == ans[i - 1]:
        start += 1
for _ in range(int(input())):
    n = int(input())
    print(ans[n])
