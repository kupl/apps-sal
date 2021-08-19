import sys
import bisect as bi
import math
from collections import defaultdict as dd
input = sys.stdin.readline


def cin():
    return list(map(int, sin().split()))


def ain():
    return list(map(int, sin().split()))


def sin():
    return input()


def inin():
    return int(input())


for _ in range(inin()):
    s = sin().strip()
    q = inin()
    a = ain()
    n = len(s)
    store = [0] * n
    store1 = [-1] * n
    f = 0
    d = dd(int)
    store[0] = 1 if s[0] == '(' else -1
    d[store[0]] = 1
    for i in range(1, n):
        if s[i] == '(':
            store[i] = store[i - 1] + 1
            d[store[i]] = i + 1
        else:
            store[i] = store[i - 1] - 1
            if d[store[i - 1]]:
                store1[d[store[i - 1]] - 1] = i + 1
    post = [-1] * n
    if n == 1 or (n == 2 and s != '()'):
        f = 1
    for i in range(n - 2, -1, -1):
        if s[i] == '(':
            if store1[i] != -1:
                post[i] = store1[i]
        else:
            post[i] = post[i + 1]
    for i in a:
        if f:
            print(-1)
        else:
            print(post[i - 1])
