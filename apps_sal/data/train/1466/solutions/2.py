#!/usr/bin/env python3

(n, q) = input().split()
n = int(n)
q = int(q)
f = [int(fi) for fi in input().split()]
cur = 0
s = [0]
for fi in f:
    cur = cur ^ fi
    s.append(cur)
for i in range(q):
    k = int(input())
    print(s[k % (n + 1)])
