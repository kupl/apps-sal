from sys import stdin, stdout
import math
import bisect
from datetime import date
from collections import Counter, deque, defaultdict
def L(): return list(map(int, stdin.readline().strip().split()))
def M(): return list(map(int, stdin.readline().strip().split()))
def I(): return int(stdin.readline().strip())
def S(): return stdin.readline().strip()
def C(): return stdin.readline().strip().split()
def pr(a): return("".join(list(map(str, a))))


def solve():
    n = I()
    a = S()
    d = Counter(a)
    ans = 0
    for i in d:
        if d[i] % 2:
            ans += 1
    print(max(0, ans - 1))


for _ in range(I()):
    solve()
