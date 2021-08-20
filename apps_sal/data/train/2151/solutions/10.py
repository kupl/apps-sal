from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from collections import defaultdict
import math
from fractions import Fraction as frac
from random import random
cin = stdin.readline


def cout(x):
    stdout.write(str(x) + '\n')


def var(type=int):
    return type(stdin.readline())


def readline(type=int):
    return list(map(type, stdin.readline().split()))


def readlist(type=int):
    return list(map(type, stdin.readline().split()))


def sorted_indexes(arr):
    return sorted(list(range(len(arr))), key=arr.__getitem__)


def printr(arr):
    [stdout.write(str(x) + ' ') for x in arr]
    cout('')


def find_lt(a, x):
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def dist(x, y):
    return math.sqrt(x * x + y * y)


def binary_search(arr, x):
    i = bisect_left(arr, x)
    if i == len(arr) or arr[i] != x:
        return -1
    return i


(n, s) = readline(int)
arr = readlist(int)
arr.sort()
count = 0
j = n // 2
if arr[j] < s:
    for i in range(j, n):
        if arr[i] < s:
            count += s - arr[i]
        else:
            break
    print(count)
else:
    for i in range(j, -1, -1):
        if arr[i] > s:
            count += arr[i] - s
        else:
            break
    print(count)
