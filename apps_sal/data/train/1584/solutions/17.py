import sys
import math
from collections import defaultdict, Counter

input = sys.stdin.readline


def print(x):
    sys.stdout.write(str(x) + "\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')


# mod=pow(10,9)+7
r, c, n = map(int, input().split())
row = [0] * r
col = [0] * c
s = set()
for i in range(n):
    x, y = map(int, input().split())
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
# mr=max(row)
# mc=max(col)
# ans=mr+mc-1
# r1=
# for i in range(r):
# 	if row[i]==mr
# ind=(0,0)
# ma=0
# for i in range(r):
# 	if row[i]>ma
# print(ans)
