# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import combinations


def run():
    N = int(input())
    A = [0] + list(map(int, sysread().split()))
    to = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, sysread().split())
        to[u].append(v)
        to[v].append(u)
    seen = [False] * (N + 1)
    dp = [float('inf')] * (N + 2)
    dp[0] = -float('inf')
    ddp2 = [0]
    paths = []
    actions = []  # (idx, pre, pro)
    ans = [0] * (N + 1)

    def dfs(node, parent=None):

        a = A[node]
        seen[node] = True
        if parent == None:
            actions.append((1, dp[1], a, 1))
            dp[1] = a
            ddp2[0] += 1
        else:
            idx = bin_search(dp, a)
            if dp[idx] == float('inf'):
                actions.append((idx, dp[idx], a, 1))
                ddp2[0] += 1
            else:
                actions.append((idx, dp[idx], a, 0))
            dp[idx] = a
        ans[node] = ddp2[0]
        for next in to[node]:
            if not seen[next]:
                dfs(next, node)

        idx, pre, pro, change = actions.pop()
        dp[idx] = pre
        ddp2[0] -= change

    dfs(1)
    for s in ans[1:]:
        print(s)
    return None


def bin_search(A, x):
    '''
    return index which is lowest in values more than or equal to x
    '''
    low = 0
    high = len(A) - 1
    c = (low + high) // 2
    if A[-1] < x:
        return float('inf')
    while high - low > 1:
        if A[c] < x:
            low = c
            c = (low + high) // 2

        elif A[c] > x:
            high = c
            c = (high + low) // 2
        else:
            return c
    return high


def __starting_point():
    run()


__starting_point()
