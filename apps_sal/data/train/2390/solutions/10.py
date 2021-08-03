#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

q = int(input())
ans = []

start = time.time()

for i in range(q):
    n = int(input())
    a = [int(j) for j in input().split()]
    d = [0 for j in range(n)]
    for j in range(n):
        d[a[j] - 1] += 1
    d.sort(reverse=True)
    s = d[0]
    last = d[0]
    for j in range(1, n):
        if last > d[j]:
            s += d[j]
            last = d[j]
        else:
            last -= 1
            if last <= 0:
                break
            s += last
    ans.append(s)

for i in range(q):
    print(ans[i])
finish = time.time()
#print(finish - start)
