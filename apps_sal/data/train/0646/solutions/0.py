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
    s = list(S())
    a = [s[0]]
    for i in range(1, len(s)):
        if a and a[-1] == s[i]:
            a.pop()
        else:
            a.append(s[i])
    print(len(a))


for _ in range(I()):
    solve()
