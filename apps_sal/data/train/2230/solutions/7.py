#!/usr/bin/env python3
from sys import stdin,stdout

def readint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()

n = int(input())
p = list(readint())
a = list(readint())
b = list(readint())

m = int(input())
c = list(readint())

cc = [[] for i in range(3)]
for i in range(n):
    cc[a[i]-1].append(i)
    cc[b[i]-1].append(i)

for i in range(3):
    cc[i].sort(key=lambda e: p[e])

ans = []
ii = [0,0,0]
for i in range(m):
    ci = c[i]-1
    while True:
        if ii[ci] >= len(cc[ci]):
            break
        if p[cc[ci][ii[ci]]] == -1:
            ii[ci] += 1
        else:
            break

    if ii[ci] >= len(cc[ci]):
        ans.append(-1)
    else:
        ans.append(p[cc[ci][ii[ci]]])
        p[cc[ci][ii[ci]]] = -1

print(*ans)



