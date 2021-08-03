#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


n = int(input())
a = input()
b = input()

start = time.time()

p00 = 0
p11 = 0
p10 = 0
p01 = 0

for i in range(n):
    if a[i] == '0':
        if b[i] == '0':
            p00 += 1
        else:
            p01 += 1
    else:
        if b[i] == '0':
            p10 += 1
        else:
            p11 += 1

ans = p00 * p11 + p10 * p01 + p00 * p10
print(ans)
finish = time.time()
#print(finish - start)
