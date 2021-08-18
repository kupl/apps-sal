import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


ceil = math.ceil
sys.setrecursionlimit(10**6)
n = ni()
A = lma()
tree = [[] for i in range(n)]
INF = 10**10
for i in range(n - 1):
    u, v = ma()
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)


def isok(num, val):
    return num < val


def bisect(ls, val):
    ok = -1
    ng = len(ls)
    x = (ok + ng) // 2
    while ng - ok > 1:
        num = ls[x]
        if isok(num, val):
            ok = x
        else:
            ng = x
        x = (ok + ng) // 2
    return ok


def LIS_1(x, ls, right):
    idx = bisect(ls, x) + 1
    if idx + 1 > right:
        ret = idx + 1
    else:
        ret = right
    rewind_idxval.append((idx, ls[idx]))
    ls[idx] = x
    return ret


def DFS_LIS(prev, ls, right):
    ans[prev] = LIS_1(A[prev], ls, right)
    for node in tree[prev]:
        if not visited[node]:
            visited[node] = True
            DFS_LIS(node, ls, ans[prev])
    idx, pval = rewind_idxval.pop()
    ls[idx] = pval


ans = [0] * n
s = 0
right = 0
rewind_idxval = collections.deque()
visited = [False] * n
visited[s] = True
ls = [INF] * n
DFS_LIS(s, ls, right)
for a in ans:
    print(a)
