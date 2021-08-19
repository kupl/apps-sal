#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b, c = list(map(int, input().split()))
n = int(input())
banks = list(map(int, input().split()))
ans = 0
for bank in banks:
    if b < bank < c:
        ans += 1
print(ans)
