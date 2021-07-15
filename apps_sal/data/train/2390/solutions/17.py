from collections import *
from sys import stdin

def input():
    return stdin.readline()

q = int(input())
for _ in range(q):
    n = int(input())
    aas = list(map(int, input().split()))
    counts = [0]*(n+1)
    for a in aas:
        counts[a] += 1
    counts.sort(reverse=True)
    total = 0
    mx = counts[0]
    for c in counts:
        inc = min(mx, c)
        if inc == 0:
            break
        mx = inc - 1
        total += inc
    print(total)

