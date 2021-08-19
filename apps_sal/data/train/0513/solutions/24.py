#import numpy as np
#import math
#from decimal import *
#from numba import njit
from bisect import bisect_left

# @njit


def main():
    N = int(input())
    a = list(map(int, input().split()))
    edges = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        edges[u] += v,
        edges[v] += u,

    ans = [0] * (N + 1)
    lastLis = []
    visited = [False] * (N + 1)
    parent = {}
    n = 1
    stack = []
    while True:
        #print(n, lastLis, stack)
        if not visited[n]:
            if len(lastLis) == 0 or a[n - 1] > lastLis[-1]:
                lastLis.append(a[n - 1])
                stack += (len(lastLis) - 1, -1),
            else:
                index = bisect_left(lastLis, a[n - 1])
                stack += (index, lastLis[index]),
                lastLis[index] = a[n - 1]
            ans[n] = len(lastLis)
            visited[n] = True
        hasNext = False
        for d in edges[n]:
            if not visited[d]:
                parent[d] = n
                n = d
                hasNext = True
        if not hasNext:
            if n == 1:
                n = 0
                break
            n = parent[n]
            # 巻き戻し
            index, value = stack.pop(len(stack) - 1)
            if value < 0:
                lastLis.pop(index)
            else:
                lastLis[index] = value

    for i in range(1, len(ans)):
        print((ans[i]))


main()
