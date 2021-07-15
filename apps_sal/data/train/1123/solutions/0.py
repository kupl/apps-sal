# cook your dish here
from sys import stdin, stdout
from math import ceil


def solve():
    for _ in range(int(input())):
        n, m = map(int, stdin.readline().split())
        par = [i for i in range(n)]
        for i in range(m):
            ta, tb = map(int, stdin.readline().strip().split())
            a, b = min(ta, tb), max(ta, tb)
            for j in range(n):
                if par[j] == par[b] and j != b:
                    par[j] = par[a]
            par[b] = par[a]

        q = int(input())
        while q:
            q -= 1
            x, y = map(int, stdin.readline().split())
            if par[x] == par[y]:
                print("YO")
            else:
                print("NO")


def __starting_point():
    solve()

__starting_point()
