from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)

def solve(G, a, lis, pre, p, ans):
    target = a[p]
    idx = bisect_left(lis, target)
    frm = lis[idx]
    to = target
    lis[idx] = to
    ans[p] = bisect_left(lis, float("inf"))
    for v in G[p]:
        if v == pre:
            continue
        solve(G, a, lis, p, v, ans)
    lis[idx] = frm

def main():
    n = int(input())
    a = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)
    lis = [float("inf")]*(n+1)
    ans = [None]*n
    solve(G, a, lis, -1, 0, ans)
    for v in ans:
        print(v)

def __starting_point():
    main()
__starting_point()
