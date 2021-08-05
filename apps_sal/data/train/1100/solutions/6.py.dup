import sys


def R(t=int): return t(eval(input()))
def RL(t=int): return [t(x) for x in input().split()]
def RLL(n, t=int): return [RL(t) for _ in range(n)]


def solve():
    p, q, r = RL()
    a, b, c = RL()
    if p > a or q > b or r > c:
        print(-1)
        return
    print(a - p + b - q + c - r)


T = R()
for t in range(1, T + 1):
    solve()
