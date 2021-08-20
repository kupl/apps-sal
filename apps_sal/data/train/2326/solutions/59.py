from itertools import product, permutations, combinations
import fractions
import heapq
import math
import sys
from collections import deque, defaultdict
import copy
import bisect
sys.setrecursionlimit(10 ** 9)


def input():
    return sys.stdin.readline().strip()


N = int(input())
a = list(map(int, input().split()))
top_list = [0]
for i in range(1, N):
    if a[i] > a[top_list[-1]]:
        top_list.append(i)
num_list = [0] * N
com = []
for i in range(len(top_list)):
    com.append(a[top_list[i]])
com.sort()
for i in range(N - 1, top_list[-1], -1):
    com.append(a[i])
com.sort()
stock = 0
for top in range(len(top_list) - 2, -1, -1):
    if top_list[top + 1] - top_list[top] > 10000:
        for i in range(top_list[top + 1] - 1, top_list[top], -1):
            com.append(a[i])
        com.sort()
    else:
        for i in range(top_list[top + 1] - 1, top_list[top], -1):
            bisect.insort(com, a[i])
    judge = 0
    total = stock * (a[top_list[top + 1]] - a[top_list[top]])
    while judge == 0:
        x = com.pop()
        if x > a[top_list[top]]:
            total += x - a[top_list[top]]
            stock += 1
        else:
            bisect.insort(com, x)
            judge = 1
    num_list[top_list[top + 1]] = total
num_list[top_list[0]] = sum(a) - sum(num_list)
for i in range(N):
    print(num_list[i])
