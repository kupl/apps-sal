import sys
from heapq import *

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def main():
    x = int(input())
    k = int(input())
    rr = LI()
    q = int(input())
    ta = LLI(q)
    timeline = []
    for r in rr:
        heappush(timeline, [r, 0, 0])
    for t, a in ta:
        heappush(timeline, [t, 1, a])
    sl = sm = 0
    sr = x
    al = 0
    ar = x
    rev_t = 0
    trend = False
    while timeline:
        t, op, a = heappop(timeline)
        sd = t - rev_t
        if op:
            if trend:
                if a < al:
                    print(min(sl + sd, x))
                elif a > ar:
                    print(min(sr + sd, x))
                else:
                    print(min(a + sm + sd, x))
            else:
                if a < al:
                    print(max(sl - sd, 0))
                elif a > ar:
                    print(max(sr - sd, 0))
                else:
                    print(max(a + sm - sd, 0))
        else:
            if trend:
                sl = min(sl + sd, x)
                sr = min(sr + sd, x)
                ar = min(ar, x - sm - sd - 1)
                sm += sd
            else:
                sl = max(sl - sd, 0)
                sr = max(sr - sd, 0)
                al = max(al, sd - sm + 1)
                sm -= sd
            trend = not trend
            rev_t = t


main()
