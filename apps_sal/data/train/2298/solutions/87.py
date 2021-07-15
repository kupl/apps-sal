#!/usr/bin/env python3

N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

d = 0
ans = 1
l = A[0]
for a in A[1:]:
    l = min(l, a)
    r = a
    if r - l == d:
        ans += 1
    elif r - l > d:
        ans = 1
        d = r - l

print(ans)

