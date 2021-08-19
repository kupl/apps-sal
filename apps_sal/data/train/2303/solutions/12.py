import math
import heapq
import itertools
import bisect
import copy
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify


def dijkstra_heap(s, edge, mask):
    dist = defaultdict(lambda: float("inf"))
    q = [s]  # 0 が会社に属していない状態
    dist[s] = 0
    d = 0
    q0 = []
    q1 = []
    while q:
        for x in q:
            if x & mask == 0:
                for y in edge[x]:
                    if dist[y[1]] <= d + y[0]:
                        continue
                    dist[y[1]] = d + y[0]
                    q1.append(y[1])
            else:
                for y in edge[x]:
                    if dist[y[1]] <= d:
                        continue
                    dist[y[1]] = d
                    q0.append(y[1])
        if q0:
            q = q0
            q0 = []
            continue
        q = q1
        q1 = []
        d += 1
    return dist


def examE(inf):
    N, M = LI()
    edge = defaultdict(list)
    # edge[i] : iから出る道の[重み,行先]の配列
    L = 32
    Mask = (1 << L) - 1
    for i in range(M):
        p, q, c = list(map(int, input().split()))
        p -= 1
        q -= 1
        p <<= L
        q <<= L
        edge[p].append((1, p + c))
        edge[p + c].append((0, p))
        edge[q].append((1, q + c))
        edge[q + c].append((0, q))
        # 同じ路線だとコスト０
        edge[p + c].append((0, q + c))
        edge[q + c].append((0, p + c))
    start = 0
    goal = (N - 1) << L
    res = dijkstra_heap(start, edge, Mask)
#    print(res)
    ans = res[goal]
    if ans == inf:
        ans = -1
    print(ans)


def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()


mod = 10**9 + 7
inf = float('inf')

examE(inf)
