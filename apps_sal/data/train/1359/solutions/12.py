from sys import stdin, stdout
import math
import bisect
from collections import Counter, deque, defaultdict
def L(): return list(map(int, stdin.readline().strip().split()))
def M(): return list(map(int, stdin.readline().strip().split()))
def I(): return int(stdin.readline().strip())
def S(): return stdin.readline().strip()
def C(): return stdin.readline().strip().split()
def pr(a): return("".join(list(map(str, a))))
#_________________________________________________#


def solve():
    n = I()
    a = L()
    e = o = 0
    for i in a:
        if i % 2:
            o += 1
        else:
            e += 1
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    ec = 0
    oc = 0
    for i in d:
        if i % 2:
            oc = max(oc, d[i])
        else:
            ec = max(ec, d[i])
    print(min(o + 2 * (e - ec), 2 * (o - oc) + e))


for _ in range(I()):
    solve()
