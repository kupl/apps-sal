import sys
from sys import stdin, stdout
from collections import deque, defaultdict
from math import ceil, floor, inf, sqrt, factorial, gcd, log2
from copy import deepcopy


def ii1():
    return int(stdin.readline().strip())


def is1():
    return stdin.readline().strip()


def iia():
    return list(map(int, stdin.readline().strip().split()))


def isa():
    return stdin.readline().strip().split()


mod = 1000000007
n = ii1()
arr = [None] * n
for ii in range(n):
    arr[ii] = iia()
count = 2
if n == 1 or n == 2:
    print(n)
else:
    flag = [0] * n
    flag[0] = -1
    flag[-1] = 1
    for i in range(1, n - 1):
        if flag[i - 1] == -1:
            if arr[i][0] - arr[i - 1][0] > arr[i][1]:
                flag[i] = -1
                count += 1
            elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
                flag[i] = 1
                count += 1
        elif flag[i - 1] == 1:
            if arr[i][0] - (arr[i - 1][0] + arr[i - 1][1]) > arr[i][1]:
                flag[i] = -1
                count += 1
            elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
                flag[i] = 1
                count += 1
        elif arr[i][0] - arr[i - 1][0] > arr[i][1]:
            flag[i] = -1
            count += 1
        elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
            flag[i] = 1
            count += 1
    print(count)
