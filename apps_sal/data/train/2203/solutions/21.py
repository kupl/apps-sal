#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


n = int(input())
a = []

for i in range(n):
    a.append(max([int(i) for i in input().split()]))

start = time.time()

for i in range(n):
    if a[i] == n - 1:
        a[i] += 1
        break

for i in a:
    print(i, end=' ')
print()

finish = time.time()
#print(finish - start)
