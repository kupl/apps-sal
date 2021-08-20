import sys
import math
from collections import defaultdict, Counter
input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + '\n')


(r, c, n) = map(int, input().split())
row = [0] * r
col = [0] * c
s = set()
for i in range(n):
    (x, y) = map(int, input().split())
    row[x] += 1
    col[y] += 1
    s.add((x, y))
ans = 0
for i in range(r):
    for j in range(c):
        cur = row[i] + col[j]
        if (i, j) in s:
            cur -= 1
        ans = max(cur, ans)
print(ans)
