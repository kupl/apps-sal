import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

s = list(input())
n = len(s)

for i in range((n-1)//2+1):
    if s[i] != s[n-2-i]:
        print(-1)
        return

if s[0] == '0':
    print(-1)
    return

if s[n-1] == '1':
    print(-1)
    return

from_ = 1
to_ = 2
ans = []
for i in range(n-1):
    ans.append((from_,to_))
    if s[i] == '1':
        from_ = to_
        to_ += 1
    else:
        to_ += 1

for a in ans:
    print(*a)
