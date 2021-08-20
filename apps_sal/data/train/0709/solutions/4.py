from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return list(map(int, stdin.readline().split()))


def I():
    return int(stdin.readline())


P = 1000000007
for t in range(I()):
    n = I()
    arr = L()
    if arr[0] >= arr[n - 1]:
        print(arr[0])
    else:
        print(arr[n - 1])
