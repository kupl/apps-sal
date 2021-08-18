from sys import stdin, stdout
import math
import bisect
from collections import Counter, deque, defaultdict
def L(): return list(map(int, stdin.readline().strip().split()))
def M(): return list(map(int, stdin.readline().strip().split()))
def I(): return int(stdin.readline().strip())
def S(): return stdin.readline().strip()
def C(): return stdin.readline().strip().split()
def pr(a): return(" ".join(list(map(str, a))))


m = 2 * pow(10, 5) + 1


def solve():
    n = I()
    a = L()
    b = [-1] * m
    c = [0] * m
    ans = 0
    for i in range(n):
        if b[a[i]] == -1:
            b[a[i]] = i
        elif i - b[a[i]] == 1:
            b[a[i]] = i
            c[a[i]] += 1
            ans = max(ans, c[a[i]])
        elif i - b[a[i]] == 2:
            b[a[i]] = i
            c[a[i]] += 1
            ans = max(ans, c[a[i]])
        else:
            b[a[i]] = i
            c[a[i]] = 0
    print(ans)


for _ in range(I()):
    solve()
