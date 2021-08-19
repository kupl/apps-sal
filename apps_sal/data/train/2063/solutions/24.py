# DSUA
import bisect
import sys
from collections import deque, namedtuple
N = 300
par = [i for i in range(N)]


def find(i):
    root = i
    while root != par[root]:
        root = par[root]
    while i != par[i]:
        newp = par[i]
        par[i] = root
        i = newp
    return root


def merge(a, b):
    a = find(a)
    b = find(b)
    par[b] = a


def main():
    n, m = map(int, input().split())
    check, ans = 0, -1
    for _ in range(n):
        l = [int(i) for i in input().split()][1:]
        check = max(check, len(l))
        for i in l:
            merge(_, n + i)
    if not check:
        print(n)
        return
    for i in range(n):
        if i == par[i]:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
